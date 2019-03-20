import nest

def init_nest(client_id, client_secret, access_token_file):

    napi = nest.Nest(client_id=client_id, client_secret=client_secret, access_token_cache_file=access_token_file)

    if napi.authorization_required:
        print('Go to ' + napi.authorize_url + ' to authorize, then enter PIN below')
        if sys.version_info[0] < 3:
            pin = raw_input("PIN: ")
        else:
            pin = input("PIN: ")
        napi.request_token(pin)

    return napi

def thermostats_iterator(napi):
    for structure in napi.structures:
        print ('Structure %s' % structure.name)
        print ('    Away: %s' % structure.away)
        print ('    Security State: %s' % structure.security_state)
        print ('    Devices:')
        for device in structure.thermostats:
            yield device

def log_thermostat_info(device):
    print ('        Device: %s' % device.name)
    print ('        Where: %s' % device.where)
    print ('            Mode       : %s' % device.mode)
    print ('            HVAC State : %s' % device.hvac_state)
    print ('            Fan        : %s' % device.fan)
    print ('            Fan Timer  : %i' % device.fan_timer)
    print ('            Temp       : %0.1fC' % device.temperature)
    print ('            Humidity   : %0.1f%%' % device.humidity)
    print ('            Target     : %0.1fC' % device.target)
    print ('            Eco High   : %0.1fC' % device.eco_temperature.high)
    print ('            Eco Low    : %0.1fC' % device.eco_temperature.low)
    print ('            hvac_emer_heat_state  : %s' % device.is_using_emergency_heat)
    print ('            online                : %s' % device.online)