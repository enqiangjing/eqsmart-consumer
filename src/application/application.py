from eqsmart.components.scan_services import ScanServices
from eqsmart.components.read_module import ReadModule
from eqsmart.main.provider import Provider
from eqlink.main.register import LinkRegister
from eqlink.main.clent import LinkClient, time_sleep, fail_server_list
from threading import Thread
from sys import path as sys_path
import traceback

sys_path.append('../..')

try:
    from src.application.configuration.conf_all import AllConf
except Exception as e:
    print(e, traceback.format_exc())
    exit(0)

'''加载配置文件'''
app_conf_profile = 'configuration/profiles/app.yaml'
AC = AllConf(app_conf_profile)

'''配置文件加载器'''
read_conf_module = ReadModule('configuration')


class Register:
    def __init__(self, path):
        """
        注册中心连接工具初始化
        :param path: 配置文件路径
        """
        ''' 注册中心的配置信息 '''
        self.link_conf = read_conf_module.read('conf_center').LinkServerConf(path).read_server()
        ''' 服务消费者配置信息 '''
        self.consumer_conf = read_conf_module.read('conf_consumer').ConsumerServerConf(path).read_server()

    def register(self):
        """
        Provider 到注册中心的注册器
        :return: Provider 服务注册器
        """
        return LinkRegister(self.link_conf)

    def keep_connect(self):
        """
        Consumer 与注册中心的连接器
        :return: 连接器
        """
        return LinkClient(self.link_conf, self.consumer_conf)


class Application:
    def __init__(self, path):
        """
        app初始化
        :param path: 配置文件路径
        """
        self.conf_path = path
        ''' Provider服务列表扫描 '''
        scan_services = ScanServices('../services')
        self.services = scan_services.get_services()
        self.services_class = scan_services.get_services_class()
        self.provider_conf = read_conf_module.read('conf_provider').ProviderServerConf(path).read_server()

    def __provider__(self):
        """
        提供服务的 Provider 启动并注册
        :return: void
        """
        print(self.provider_conf)
        Provider(self.provider_conf, self.services, self.services_class).server_init(
            Register(self.conf_path).register().register_int)

    def __connect_link__(self):
        """ Consumer 启动并保持与注册中心的连接 """
        ''' 实例化一个消费者注册器 '''
        consumer_register = Register(self.conf_path)
        ''' Consumer到注册中心的连接器 '''
        consumer_connect = consumer_register.keep_connect()
        ''' Consumer与注册中心断线重连的配置 '''
        reconnect_alive = consumer_register.consumer_conf['reconnect_alive']
        reconnect_count = consumer_register.consumer_conf['reconnect_count']
        ''' 重连计数，Consumer连接结果 '''
        c_count, c_result = 0, ''
        ''' 设置循环，进行连接重试 '''
        while c_count < reconnect_count:
            ''' 获取Consumer与注册中心的连接结果 '''
            c_result = consumer_connect.client_int({'type': 'get provider', 'fail_server': fail_server_list})
            ''' 等待一段时间后，再次重连 '''
            time_sleep(reconnect_alive)
            ''' 根据不同的返回类型，设置重连计数器 '''
            c_count = 1 if c_result == 'send fail' else (c_count + 1)
            print(
                f"[app] Consumer断线重连, 次数: {str(c_count)}。重试总次数: {str(reconnect_count)}，等待时长: {str(reconnect_alive)}")


def main():
    """ 应用启动 """
    Thread(target=Application('configuration/profiles/app.yaml').__provider__).start()
    Thread(target=Application('configuration/profiles/app.yaml').__connect_link__).start()


if __name__ == '__main__':
    main()
