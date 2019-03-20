from influxdb import InfluxDBClient
from influxdb import SeriesHelper

class ThermostatHelper(SeriesHelper):
    class Meta:
        series_name = 'nest.stats'
        fields = ['temperature', 'humidity', 'target', 'state', 'eco_high', 'eco_low']
        tags = ['device_name']