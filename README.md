# eqsmart-consumer
基于eqsmart，服务消费者示例。

**框架**
```
# 注册中心框架
https://github.com/enqiangjing/eqlink

# 微服务框架
https://github.com/enqiangjing/eqsmart
```
**示例工程**
```
# 注册中心服务示例
https://github.com/enqiangjing/eqlink-server

# 微服务 服务提供者 Provider
https://github.com/enqiangjing/eqsmart-provider

# 微服务 服务消费者 Consumer（同时也是服务提供者）
https://github.com/enqiangjing/eqsmart-consumer

# 微服务 服务网关 Gateway（同时也是服务消费者）
https://github.com/enqiangjing/eqsmart-gateway
```

## 服务启动
```shell script
# 直接启动：会根据 app.yaml 中 app.env 判断运行环境
python application.py
# 指定运行环境
python application.py env=dev
# 指定运行端口
python application.py port=7801
```

## * 免责声明
* 本项目所有内容仅供参考和学习交流使用。
* 项目所存在的风险将由使用者自行承担，因使用本项目而产生的一切后果也由使用者自己承担。
* 凡以任何方式直接、间接使用本项目的人员，视为自愿接受本项目声明和法律法规的约束。