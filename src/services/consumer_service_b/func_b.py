from eqsmart.main.remote_call import RemoteCall
from src.application.application import AC


def service(a, b):
    remote_response = RemoteCall('provider_service_b/func_b').func_call(('ba', 'bb'))
    res = {
        'remote_b': remote_response,
        'func_consumer_b': str(a) + ' -- ' + str(b),
        'application_name': AC.read_conf('app.application.name')
    }
    return res
