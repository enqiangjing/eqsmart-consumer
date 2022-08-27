import sys
from eqsmart.components.load_conf import LoadConf, get_run_params


class LinkServerConf(LoadConf):
    def __init__(self, path):
        super().__init__(path, get_run_params(sys.argv[1:]))

    def read_server(self):
        return {
            'IP': self.node_read('eqlink.ip'),
            'PORT': self.node_read('eqlink.port'),
            'BUF_SIZE': self.node_read('eqlink.buf_size'),
            'BACKLOG': self.node_read('eqlink.backlog')
        }
