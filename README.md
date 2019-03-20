# nest-monitoring
Gather data from nest thermostat and send to influxdb

create a file with credentials: ~/.nest-monitor-credentials.json

put the following in the config file with your nest creds: {"client_id": "your_client_id", "client_secret": "your_client_secret"} 

clone repo and cd into it

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt 

python src/nest_monitor.py 