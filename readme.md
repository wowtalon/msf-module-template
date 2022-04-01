# MSF 模块开发模板

## 开发环境搭建

```bash

$ git clone https://github.com/wowtalon/msf-module-template.git

$ cd msf-module-template

$ python3 -m venv venv

$ source venv/bin/activate

```

## 使用方法

```bash

$ mkdir -p ~/.msf4/modules/auxiliary/mymodules/

$ cp poc/poc.py ~/.msf4/modules/auxiliary/mymodules/

```

## 在 MSF 中加载模块

```bash

$ msfconsole

msf6 > reload_all

msf6 > search mymodules

msf6 > use auxiliary/mymodules/poc

```


## 参考连接

+ [Running-Private-Modules](https://github.com/rapid7/metasploit-framework/wiki/Running-Private-Modules)

+ [Writing Python Modules for Metasploit](https://github.com/rapid7/metasploit-framework/wiki/Writing-External-Python-Modules)