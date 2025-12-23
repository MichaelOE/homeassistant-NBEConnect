from logging import getLogger

from homeassistant.components.button import ButtonEntity
from homeassistant.core import callback
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import RTBDataCoordinator
from .const import DOMAIN
from .protocol import Proxy

34
_LOGGER = getLogger(__name__)


async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN][config_entry.entry_id + "_coordinator"]
    proxy = hass.data[DOMAIN][config_entry.entry_id]

    async_add_entities(
        [
            RTBSignalButton(
                coordinator,
                proxy,
                "Start Boiler",
                "settings/misc/start",
                "nbestart",
                "1",
            ),
            RTBSignalButton(
                coordinator, proxy, "Stop Boiler", "settings/misc/stop", "nbestop", "1"
            ),
            RTBSignalButton(
                coordinator,
                proxy,
                "Reset Boiler Alarm",
                "settings/misc/reset_alarm",
                "nbereset",
                "1",
            ),
        ]
    )


class RTBSignalButton(CoordinatorEntity, ButtonEntity):
    """Representation of a signal switch."""

    def __init__(self, coordinator: RTBDataCoordinator, proxy, name, path, uid, value):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._name = name
        self.coordinator = coordinator
        self._state = False
        self.proxy = proxy
        self._path = path
        self._value = value
        self.uid = uid

    @property
    def name(self):
        """Return the name of the switch."""
        return self._name

    @property
    def device_info(self):
        """Return device information about this entity."""
        _LOGGER.debug("StokerCloudSensor: device_info")

        return {
            "identifiers": {(DOMAIN, self.coordinator.proxy.serial)},
            "manufacturer": "NBE",
            "model": "NBE RTB",
            "name": self.coordinator.proxy.serial,
        }

    @property
    def unique_id(self):
        return self.uid

    def press(self) -> None:
        """Press the button."""
        _LOGGER.debug(f"asynch press {self._name} - awaiting sendboilercmd..")
        self.proxy.set(self._path, self._value)
        _LOGGER.debug(f"asynch press {self._name} - Done!")
