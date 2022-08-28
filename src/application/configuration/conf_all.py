import sys
from eqsmart.components.load_conf import LoadConf, get_run_params


class AllConf(LoadConf):
    def __init__(self, path):
        super().__init__(path, get_run_params(sys.argv[1:]))

    def read_conf(self, node):
        """
        配置节点读取
        :param node: 节点名称，如 a.b.c
        :return: 节点值
        """
        return self.node_read(node)
