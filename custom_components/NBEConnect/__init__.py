from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry
from .const import DOMAIN, PLATFORMS
from .rtbdata import RTBData
from .protocol import Proxy
import datetime
import logging

PORT = 8483

logger = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the component."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data.setdefault(DOMAIN, {})  # Ensure DOMAIN key exists in hass.data
    hass.data[DOMAIN][entry.entry_id] = Proxy(
        entry.data["password"], PORT, entry.data["ip_address"], entry.data["serial"]
    )
    logger.debug("Starting poller.... ")
    logger.debug("PW %s", entry.data["password"])
    logger.debug("IP %s", entry.data["ip_address"])
    logger.debug("Serial %s", entry.data["serial"])

    coordinator = RTBDataCoordinator(
        hass, entry.entry_id, hass.data[DOMAIN][entry.entry_id]
    )
    hass.data[DOMAIN][entry.entry_id + "_coordinator"] = coordinator

    await coordinator.async_config_entry_first_refresh()
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_forward_entry_unload(
        entry, PLATFORMS
    ):
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok


class RTBDataCoordinator(DataUpdateCoordinator):
    """Class to manage fetching RTB data."""

    def __init__(self, hass, entry_id, proxy):
        """Initialize the data coordinator."""
        self.hass = hass
        self.entry_id = entry_id
        self.proxy = proxy
        self.rtbdata = RTBData([])
        update_interval = datetime.timedelta(seconds=60)  # Set the update interval
        super().__init__(hass, logger, name=DOMAIN, update_interval=update_interval)

    async def _async_update_data(self):
        """Fetch the latest data from the device."""
        try:
            operating_data = await self.hass.async_add_executor_job(
                self.proxy.get, "operating_data/"
            )
            consumption_data = await self.hass.async_add_executor_job(
                self.proxy.get, "consumption_data/counter"
            )
            # Read hopper content from settings to reflect exact integer set value
            hopper_setting = None
            try:
                hopper_setting = await self.hass.async_add_executor_job(
                    self.proxy.get, "settings/hopper/content"
                )
            except Exception:
                # If settings read fails, continue without it
                hopper_setting = None
            logger.debug(operating_data)
            logger.debug(consumption_data)
            logger.debug(hopper_setting)
            if operating_data is not None:
                if consumption_data is not None:
                    operating_data = operating_data + consumption_data
                # Append settings value in key=value form so RTBData.get can retrieve it
                if hopper_setting and len(hopper_setting) > 0 and hopper_setting[0] is not None:
                    try:
                        operating_data.append(
                            f"settings/hopper/content={hopper_setting[0]}"
                        )
                    except Exception:
                        # Keep integration resilient if unexpected value format
                        pass
                self.rtbdata.set(operating_data)
            return operating_data
        except TimeoutError as e:
            logger.warning(
                "Timeout occurred while fetching RTB data. Integration will continue without data."
            )
            return None
