import sys
from eqsmart.components.load_conf import LoadConf, get_run_params


class ProviderServerConf(LoadConf):
    def __init__(self, path):
        super().__init__(path, get_run_params(sys.argv[1:]))

    def read_server(self):
        return {
            'PORT': self.node_read('provider.port'),
            'BUF_SIZE': self.node_read('provider.buf_size'),
            'BACKLOG': self.node_read('provider.backlog'),
            'WEIGHT': self.node_read('provider.weight'),
            'IP': self.node_read('provider.ip'),
            'HOST': self.node_read('provider.host')
        }
