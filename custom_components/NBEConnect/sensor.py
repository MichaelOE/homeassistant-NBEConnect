from logging import getLogger

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from . import RTBDataCoordinator
from .const import DOMAIN, MANUFACTURER, MODEL
from .protocol import Proxy
from .rtbdata import RTBData

_LOGGER = getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the NBE-RTB sensors."""
    _LOGGER.info("This is debugging from sensor.py")

    # DataUpdateCoordinator
    dc = hass.data[DOMAIN][entry.entry_id + "_coordinator"]

    async_add_entities(
        [
            RTBBinarySensor(
                dc,
                "Boiler Running",
                "operating_data/power_pct",
                "boiler_power_pct",
                BinarySensorDeviceClass.HEAT,
            ),
            RTBBinarySensor(
                dc,
                "Boiler Alarm",
                "operating_data/off_on_alarm",
                "boiler_state_off_on_alarm",
                BinarySensorDeviceClass.PROBLEM,
            ),
            RTBSensor(
                dc,
                "Boiler Temperature",
                "operating_data/boiler_temp",
                "boiler_temp",
                "\u00b0C",
                SensorDeviceClass.TEMPERATURE,
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "DWH Temperature",
                "operating_data/dhw_temp",
                "dhw_temp",
                "\u00b0C",
                SensorDeviceClass.TEMPERATURE,
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "External Temperature",
                "operating_data/external_temp",
                "external_temp",
                "\u00b0C",
                SensorDeviceClass.TEMPERATURE,
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "Boiler Effect",
                "operating_data/power_kw",
                "power_kw",
                "kW",
                SensorDeviceClass.POWER,
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "Boiler Power",
                "operating_data/power_pct",
                "power_pct",
                "%",
                SensorDeviceClass.POWER_FACTOR,
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "Total Consumption",
                "consumption_data/counter",
                "pelletcounter",
                "kg",
                SensorDeviceClass.WEIGHT,
                SensorStateClass.TOTAL_INCREASING,
            ),
            RTBSensor(
                dc,
                "Smoke Temperature",
                "operating_data/smoke_temp",
                "smoke_temp",
                "\u00b0C",
                SensorDeviceClass.TEMPERATURE,
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "Return Temperature",
                "operating_data/return_temp",
                "return_temp",
                "\u00b0C",
                SensorDeviceClass.TEMPERATURE,
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "Shaft Temperature",
                "operating_data/shaft_temp",
                "shaft_temp",
                "\u00b0C",
                SensorDeviceClass.TEMPERATURE,
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "Photo Sensor",
                "operating_data/photo_level",
                "photo_level",
                "lx",
                SensorDeviceClass.ILLUMINANCE,
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "O2",
                "operating_data/oxygen",
                "oxygen",
                "%",
                "",
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "O2 Taget",
                "operating_data/oxygen_ref",
                "oxygen_ref",
                "%",
                "",
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "Contoler Time",
                "operating_data/time",
                "time",
                "",
                SensorDeviceClass.DATE,
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "T4 Temperature",
                "operating_data/t4_temp",
                "t4_temp",
                "\u00b0C",
                SensorDeviceClass.TEMPERATURE,
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "T5 Temperature",
                "operating_data/t5_temp",
                "t5_temp",
                "\u00b0C",
                SensorDeviceClass.TEMPERATURE,
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "T6 Temperature",
                "operating_data/t6_temp",
                "t6_temp",
                "\u00b0C",
                SensorDeviceClass.TEMPERATURE,
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "T7 Temperature",
                "operating_data/t7_temp",
                "t7_temp",
                "\u00b0C",
                SensorDeviceClass.TEMPERATURE,
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "Distance to Pellets",
                "operating_data/distance",
                "distance",
                "cm",
                SensorDeviceClass.DISTANCE,
                SensorStateClass.MEASUREMENT,
            ),
            # operating_data/milli_ampere
            RTBSensor(
                dc,
                "Flow",
                "operating_data/flow1",
                "flow1",
                "l/h",
                "",
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "Flow 2",
                "operating_data/flow2",
                "flow2",
                "l/h",
                "",
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "Flow 3",
                "operating_data/flow3",
                "flow3",
                "l/h",
                "",
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "Flow 4",
                "operating_data/flow4",
                "flow4",
                "l/h",
                "",
                SensorStateClass.MEASUREMENT,
            ),
            # operating_data/mean_out_temp
            # operating_data/forward_ref
            # operating_data/sun2_temp=
            # operating_data/sun_surplus_temp
            RTBSensor(
                dc,
                "Air Pressure",
                "operating_data/pressure",
                "pressure",
                "bar",
                SensorDeviceClass.PRESSURE,
                SensorStateClass.MEASUREMENT,
            ),
            RTBSensor(
                dc,
                "Air Flow",
                "operating_data/air_flow",
                "air_flow",
                "m3/h",
                SensorDeviceClass.VOLUME_FLOW_RATE,
                SensorStateClass.MEASUREMENT,
            ),
            # operating_data/sun_temp
            # operating_data/house_valve_state
            # operating_data/chill_out
            # operating_data/sun_pumpspeed
            # operating_data/sun_power_kw
            # operating_data/cloud_level
            # operating_data/forward_temp
            # operating_data/back_pressure
            # operating_data/t1_temp
            # operating_data/air_quality
            # operating_data/feed_low
            # operating_data/feed_medium
            # operating_data/feed_high
            RTBSensor(
                dc,
                "Hopper content kg",
                "operating_data/content",
                "content",
                "kg",
                SensorDeviceClass.WEIGHT,
                SensorStateClass.MEASUREMENT,
            ),
            # operating_data/state
            # operating_data/substate
            RTBBinarySensor(
                dc,
                "Boiler Pump",
                "operating_data/boiler_pump_state",
                "boiler_pump_state",
                BinarySensorDeviceClass.RUNNING,
            ),
            RTBBinarySensor(
                dc,
                "Dhw Valve",
                "operating_data/dhw_valve_state",
                "dhw_valve_state",
                BinarySensorDeviceClass.RUNNING,
            ),
            RTBBinarySensor(
                dc,
                "House Pump",
                "operating_data/house_pump_state",
                "house_pump_state",
                BinarySensorDeviceClass.RUNNING,
            ),
            # operating_data/sun_pump_state
            # operating_data/sun_surplus_state
            # operating_data/ashbox_minutes
            # operating_data/ashbox_contact
            RTBSensor(
                dc,
                "Internet Uptime",
                "operating_data/internet_uptime",
                "internet_uptime",
                "%",
                SensorDeviceClass.POWER_FACTOR,
                SensorStateClass.MEASUREMENT,
            ),
            # RTBBinarySensor(dc, 'off_on_alarm', 'operating_data/off_on_alarm', 'off_on_alarm', BinarySensorDeviceClass.PROBLEM),
            RTBBinarySensor(
                dc,
                "Contact 1",
                "operating_data/contact1",
                "contact1",
                BinarySensorDeviceClass.RUNNING,
            ),
            RTBBinarySensor(
                dc,
                "Contact 2",
                "operating_data/contact2",
                "contact2",
                BinarySensorDeviceClass.RUNNING,
            ),
            # operating_data/dl_progress
            # operating_data/substate_sec
            # operating_data/corr_low
            # operating_data/corr_medium
            # operating_data/corr_high
            # operating_data/ash_clean
        ]
    )

    # async_add_entities(
    #     [
    #         RTBBinarySensor(
    #             dc,
    #             "Boiler Running",
    #             "operating_data/power_pct",
    #             "boiler_power_pct",
    #             BinarySensorDeviceClass.HEAT,
    #         ),
    #         RTBBinarySensor(
    #             dc,
    #             "Boiler Alarm",
    #             "operating_data/off_on_alarm",
    #             "boiler_state_off_on_alarm",
    #             BinarySensorDeviceClass.PROBLEM,
    #         ),
    #         RTBSensor(
    #             dc,
    #             "Boiler Temperature",
    #             "operating_data/boiler_temp",
    #             "boiler_temp",
    #             "\u00b0C",
    #             SensorDeviceClass.TEMPERATURE,
    #             SensorStateClass.MEASUREMENT,
    #         ),
    #         RTBSensor(
    #             dc,
    #             "DWH Temperature",
    #             "operating_data/sun_dhw_temp",
    #             "dhw_temp",
    #             "\u00b0C",
    #             SensorDeviceClass.TEMPERATURE,
    #             SensorStateClass.MEASUREMENT,
    #         ),
    #         RTBSensor(
    #             dc,
    #             "External Temperature",
    #             "operating_data/external_temp",
    #             "external_temp",
    #             "\u00b0C",
    #             SensorDeviceClass.TEMPERATURE,
    #             SensorStateClass.MEASUREMENT,
    #         ),
    #         RTBSensor(
    #             dc,
    #             "Boiler Effect",
    #             "operating_data/power_kw",
    #             "power_kw",
    #             "kW",
    #             SensorDeviceClass.POWER,
    #             SensorStateClass.MEASUREMENT,
    #         ),
    #         RTBSensor(
    #             dc,
    #             "Boiler Power",
    #             "operating_data/power_pct",
    #             "power_pct",
    #             "%",
    #             SensorDeviceClass.POWER_FACTOR,
    #             SensorStateClass.MEASUREMENT,
    #         ),
    #         RTBSensor(
    #             dc,
    #             "Total Consumption",
    #             "consumption_data/counter",
    #             "pelletcounter",
    #             "kg",
    #             SensorDeviceClass.WEIGHT,
    #             SensorStateClass.TOTAL_INCREASING,
    #         ),
    #     ]
    # )

    _LOGGER.info(f"Sensor.py, sensors where added!")


class RTBSensor(CoordinatorEntity, SensorEntity):
    """Representation of an RTB sensor."""

    def __init__(
        self,
        coordinator: RTBDataCoordinator,
        name,
        client_key,
        uid,
        unitofmeassurement,
        device_class,
        state_class,
    ):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.coordinator = coordinator
        self.client_key = client_key
        self._device_class = device_class
        self.sensorname = name
        self.uid = uid
        self._unit_of_measurement = unitofmeassurement
        self._state_class = state_class

    @property
    def device_info(self):
        """Return device information about this entity."""
        _LOGGER.debug("NBESensor: device_info")

        return {
            "identifiers": {(DOMAIN, self.coordinator.proxy.serial)},
            "manufacturer": MANUFACTURER,
            "model": MODEL,
            "name": self.coordinator.proxy.serial,
        }

    @property
    def name(self):
        """Return the name of the sensor."""
        # _LOGGER.info(f"sensor.py (name) returning \"NBE {self.sensorname}\"")
        return f"NBE {self.sensorname}"

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of the sensor."""
        return self._unit_of_measurement

    @property
    def unique_id(self):
        return self.uid

    @property
    def state(self):
        """Return the state of the sensor."""
        state = self.coordinator.rtbdata.get(self.client_key)
        # _LOGGER.info(f"Sensor.py RTBSensor (state) returning \"{state}\"")
        return state

    @property
    def device_class(self):
        """Return the device class of the sensor."""
        return self._device_class

    @property
    def state_class(self):
        """Return the state class of the sensor."""
        return self._state_class


class RTBBinarySensor(CoordinatorEntity, BinarySensorEntity):
    """Representation of an RTB binary sensor."""

    def __init__(self, coordinator, name, client_key, uid, device_class):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self.client_key = client_key
        self._device_class = device_class
        self.sensorname = name
        self.uid = uid

    @property
    def name(self):
        """Return the name of the binary sensor."""
        # _LOGGER.info(f"sensor.py RTBBinarySensor (name) returning \"NBE {self.sensorname}\"")
        return f"NBE {self.sensorname}"

    @property
    def is_on(self):
        _LOGGER.debug("is_on called")
        """Return the state of the binary sensor."""
        s = self.coordinator.rtbdata.get(self.client_key)
        _LOGGER.debug(f'sensor.py RTBBinarySensor (is_on) value "{s}"')
        if "power_pct" in self.client_key:
            return s != "0"
        if "off_on_alarm" in self.client_key:
            return s == "2"
        return s == "0"

    @property
    def unique_id(self):
        return self.uid

    @property
    def device_class(self):
        """Return the device class of the binary sensor."""
        return self._device_class


# BINARYSENSORS_BOILER: tuple[RTBBinarySensor, ...] = (
#             RTBBinarySensor(
#                 dc,
#                 "Boiler Running",
#                 "operating_data/power_pct",
#                 "boiler_power_pct",
#                 BinarySensorDeviceClass.HEAT,
#             ),
#             RTBBinarySensor(
#                 dc,
#                 "Boiler Alarm",
#                 "operating_data/off_on_alarm",
#                 "boiler_state_off_on_alarm",
#                 BinarySensorDeviceClass.PROBLEM,
#             ),
# )
# SENSORS_BOILER: tuple[RTBSensor, ...] = (
#             RTBSensor(
#                 dc,
#                 "Boiler Temperature",
#                 "operating_data/boiler_temp",
#                 "boiler_temp",
#                 "\u00b0C",
#                 SensorDeviceClass.TEMPERATURE,
#                 SensorStateClass.MEASUREMENT,
#             ),
#             RTBSensor(
#                 dc,
#                 "DWH Temperature",
#                 "operating_data/sun_dhw_temp",
#                 "dhw_temp",
#                 "\u00b0C",
#                 SensorDeviceClass.TEMPERATURE,
#                 SensorStateClass.MEASUREMENT,
#             ),
#             RTBSensor(
#                 dc,
#                 "External Temperature",
#                 "operating_data/external_temp",
#                 "external_temp",
#                 "\u00b0C",
#                 SensorDeviceClass.TEMPERATURE,
#                 SensorStateClass.MEASUREMENT,
#             ),
#             RTBSensor(
#                 dc,
#                 "Boiler Effect",
#                 "operating_data/power_kw",
#                 "power_kw",
#                 "kW",
#                 SensorDeviceClass.POWER,
#                 SensorStateClass.MEASUREMENT,
#             ),
#             RTBSensor(
#                 dc,
#                 "Boiler Power",
#                 "operating_data/power_pct",
#                 "power_pct",
#                 "%",
#                 SensorDeviceClass.POWER_FACTOR,
#                 SensorStateClass.MEASUREMENT,
#             ),
#             RTBSensor(
#                 dc,
#                 "Total Consumption",
#                 "consumption_data/counter",
#                 "pelletcounter",
#                 "kg",
#                 SensorDeviceClass.WEIGHT,
#                 SensorStateClass.TOTAL_INCREASING,
#             ),
#     )
