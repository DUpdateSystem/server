# [UpgradeAll Server](https://github.com/DUpdateSystem/Server)

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

UpgradeAll 服务端代码仓库

该项目旨在为 [UpgradeAll 项目](https://github.com/DUpdateSystem/UpgradeAll) 提供数据支持。
它由以下部分构成
1. 服务端主体。
2. 软件源脚本仓库。

## 内容列表

- [背景](#背景)
- [安装](#安装)
- [使用说明](#使用说明)
   - [运行这个项目](#运行这个项目)
      - [Docker Compose](#docker-compose)
      - [手动安装并运行](#shell-script)
- [相关仓库](#相关仓库)
- [维护者](#维护者)
- [如何贡献](#如何贡献)
- [使用许可](#使用许可)

## 背景

`UpgradeAll 服务端` 最开始因为 [@yah](https://github.com/wangxiaoerYah) 在维护脚本时发觉本地爬虫的效率问题而被提出，并于 [0.1.2 版本（客户端版本）](https://github.com/DUpdateSystem/UpgradeAll/releases/tag/0.1.2-rc.2)的开发阶段实现。


## 安装

这个项目使用 [Python 3](https://www.python.org/)。请确保你本地安装了它们。
> **TIPS**：gRPC proto 编译命令（在 server 目录下执行）：
``` bash
python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./app/grpc_template/route.proto
```


## 使用说明

克隆仓库，这样你就可以开始使用该项目了

```sh
$ git clone --depth=1 https://github.com/DUpdateSystem/Server.git
# 获取你的调试/开发的基础环境
$ cd server
# 进入 Server 主体代码文件夹
```

### 运行这个项目

#### Docker Compose
```sh
# 在项目根目录下
$ docker-compose -f oci_build/docker-compose.yml
```

#### Shell script
> 不推荐使用
该脚本只用于调试，脚本会自动本地编译新的 Docker 镜像并挂载代码文件夹以便调试
```sh
$ ./startup.sh
# 部署服务端
$ ./startup.sh --debug 6a6d590b-1809-41bf-8ce3-7e3f6c8da945 --test_options android_app_package com.nextcloud.client
# 测试软件源
```
#### 手动运行
##### 数据库
1. 按照 oci_build/db.env 设置 mariadb 初始环境（主要是用户/密码），然后运行它
2. 使用 Docker/Podman 运行数据库
```sh
# 在项目根目录下
$ docker run --rm --name=upa-db --env-file oci_build/db.env -v $PWD/db_data/:/var/lib/mysql -p 3306:3306 mariadb
```
###### 服务端
1. 安装 Python 依赖
```sh
# 在项目根目录下
pip install -r server/requirements.txt
```
2. 部署
```sh
# 在项目根目录下
$ ../scripts/boot.sh proxy  # 启动中间件
$ ../scripts/boot.sh getter # 启动后端
$ ../scripts/boot.sh hello  # 启动 API 前端
$ curl -w "%{http_code}\n" localhost:5255/about # 测试服务端
```

## 相关仓库

- [UpgradeAll](https://github.com/DUpdateSystem/UpgradeAll) — UpgradeAll 的安卓实现。
- [UpgradeAll-rules](https://github.com/DUpdateSystem/UpgradeAll-rules) — UpgradeAll 的配置文件仓库。

## 维护者

[@xz-dev](https://github.com/xz-dev)。

## 如何贡献

非常欢迎你的加入！[官方文档-参与我们](https://upgradeall.now.sh/joinus/)  
你已经有一个明确的想法了?请 [提一个 Issue](https://github.com/DUpdateSystem/Server/issues/new/choose) 或者提交一个 Pull Request。


## 使用许可

[GPL-3.0](LICENSE) © xz-dev
