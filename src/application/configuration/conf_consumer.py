import sys
from eqsmart.components.load_conf import LoadConf, get_run_params


class ConsumerServerConf(LoadConf):
    def __init__(self, path):
        super().__init__(path, get_run_params(sys.argv[1:]))

    def read_server(self):
        return {
            'alive': self.node_read('consumer.alive'),
            'reconnect_count': self.node_read('consumer.reconnect.count'),
            'reconnect_alive': self.node_read('consumer.reconnect.alive')
        }
