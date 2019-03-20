import sys
import os
import config_helper
import nest_helper
from pathlib import Path
from influxdb import InfluxDBClient
from influx_helper import ThermostatHelper

credentials_file = os.path.join(str(Path.home()), '.nest-monitor-credentials.json')
access_token_file = os.path.join(str(Path.home()), '.nest-monitor-access-token.json')

(client_id, client_secret) = config_helper.read_client_credentials(credentials_file)

nest_client = nest_helper.init_nest(client_id, client_secret, access_token_file)

influx_client = InfluxDBClient('localhost', 8086, '', '', 'nest')

for device in nest_helper.thermostats_iterator(nest_client):        
    nest_helper.log_thermostat_info(device)
    ThermostatHelper(device_name=device.name, 
        temperature=device.temperature, 
        humidity=device.humidity, 
        eco_high=device.eco_temperature.high,
        eco_low=device.eco_temperature.low, 
        state=0 if device.hvac_state == "off" else 1)

ThermostatHelper.commit(influx_client)


