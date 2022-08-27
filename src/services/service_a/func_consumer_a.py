from eqsmart.main.remote_call import RemoteCall
from src.application.application import AC


def service(a, b):
    remote_response = RemoteCall('provider_service_a/func_a').func_call(('aa', 'ab'))
    res = {
        'remote_a': remote_response,
        'func_consumer_a': str(a) + ' -- ' + str(b),
        'application_name': AC.read_conf('app.application_name')
    }
    return res
