from logging import getLogger

from homeassistant.components.number import NumberEntity, NumberDeviceClass
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, MANUFACTURER, MODEL
from .protocol import Proxy

_LOGGER = getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the NBE-RTB number entities."""
    _LOGGER.info("Setting up NBE number entities")

    # DataUpdateCoordinator and Proxy
    dc = hass.data[DOMAIN][entry.entry_id + "_coordinator"]
    proxy = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            RTBNumber(
                dc,
                proxy,
                "Boiler Temperature Setpoint",
                "operating_data/boiler_ref",
                "settings/boiler/temp",
                "boiler_ref",
                "\u00b0C",
                NumberDeviceClass.TEMPERATURE,
                min_value=30,
                max_value=90,
                step=1,
            ),
            RTBNumber(
                dc,
                proxy,
                "DWH Temperature Setpoint",
                "operating_data/dhw_ref",
                "settings/hot_water/temp",
                "dhw_ref",
                "\u00b0C",
                NumberDeviceClass.TEMPERATURE,
                min_value=30,
                max_value=90,
                step=1,
            ),
        ]
    )

    _LOGGER.info("Number entities added successfully")


class RTBNumber(CoordinatorEntity, NumberEntity):
    """Representation of an RTB number entity."""

    def __init__(
        self,
        coordinator,
        proxy: Proxy,
        name,
        state_key,
        control_path,
        uid,
        unit,
        device_class,
        min_value=0,
        max_value=100,
        step=1,
    ):
        """Initialize the number entity."""
        super().__init__(coordinator)
        self.coordinator = coordinator
        self.proxy = proxy
        self._name = name
        self._state_key = state_key
        self._control_path = control_path
        self._uid = uid
        self._unit = unit
        self._device_class = device_class
        self._attr_native_min_value = min_value
        self._attr_native_max_value = max_value
        self._attr_native_step = step

    @property
    def device_info(self):
        """Return device information about this entity."""
        return {
            "identifiers": {(DOMAIN, self.coordinator.proxy.serial)},
            "manufacturer": MANUFACTURER,
            "model": MODEL,
            "name": self.coordinator.proxy.serial,
        }

    @property
    def name(self):
        """Return the name of the number entity."""
        return f"NBE {self._name}"

    @property
    def unique_id(self):
        """Return unique ID."""
        return self._uid

    @property
    def native_unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit

    @property
    def device_class(self):
        """Return the device class."""
        return self._device_class

    @property
    def native_value(self):
        """Return the current value."""
        value = self.coordinator.rtbdata.get(self._state_key)
        if value is not None:
            try:
                return float(value)
            except (ValueError, TypeError):
                _LOGGER.warning(f"Could not convert value '{value}' to float")
                return None
        return None

    async def async_set_native_value(self, value: float) -> None:
        """Set new value."""
        _LOGGER.info(f"Setting {self._name} to {value}")
        try:
            # Convert float to string for the protocol and run in executor
            await self.hass.async_add_executor_job(
                self.proxy.set, self._control_path, str(int(value))
            )
            # Request coordinator update to reflect the change
            await self.coordinator.async_request_refresh()
        except Exception as e:
            _LOGGER.error(f"Failed to set {self._name}: {e}")
