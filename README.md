## 前言
耗费了一周的时间，才将这款信息收集工具写出来，虽然现在功能还不完善，但我会一直维护，使它会变得更好。
[time:2019-10-28]
## 功能
功能还不完善，现在仅仅能做一些简单的信息收集，如：
+ 收集子域名站点的IP地址
+ 收集主域名下有哪些子域名
+ 收集子域名站点的标题信息
+ 收集子域名的物理地址信息
+ 确定子域名站点是否使用了CDN
+ 收集子域名站点开放了哪些端口
+ 收集子域名站点开放了哪些服务
+ 收集子域名站点使用了哪种系统
+ 收集子域名站点使用了哪种CMS
+ 收集子域名站点使用了哪种中间件
+ 收集子域名站点使用了哪种数据库
+ 收集子域名站点使用了哪种脚本语言

注：收集的信息可能会有些不准确，后面会慢慢改善。
## 使用
```angular2
Usage: Nict.py [OPTIONS]

  Easy to use internet information collection tool

Options:
  --target TEXT            设置扫描目标(现在仅支持域名扫描)
  --threads INTEGER RANGE  设置运行线程(默认开启200线程)
  --process INTEGER RANGE  设置运行进程(默认开启4个进程)
  --timeout INTEGER        设置超时时间(默认超时时间为5秒)
  --output TEXT            设置文件保存路径(默认为output目录下result.txt文件)
  --help                   查看使用帮助且退出

```
![Screenshot](https://github.com/CJero/Nict/blob/master/Screenshot.png)
## 更新
+ v1.0 初始版本
## 最后
喜欢就点亮star哇&欢迎大家反馈建议和BUG。
项目地址:https://github.com/CJero/
