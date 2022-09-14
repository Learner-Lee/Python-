import pywifi
from pywifi import const  # 引用一些常量


# 判断是否已经链接到WiFi
def gic():
    # 创建一个无线对象
    wifi = pywifi.PyWiFi()
    # 获取到第一个无线网卡
    ifaces = wifi.interfaces()[0]
    # 打印网卡的名称
    print(ifaces.name())
    # 列表
    print(ifaces)
    # 打印网卡链接状态， 0 未连接到WiFi环境     4 已连接
    print(ifaces.status())
    if ifaces.status() == const.IFACE_CONNECTED:
        print("已连接")
    else:
        print("未连接")


# 扫描附近的WiFi
def bies():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    # 扫描WiFi
    ifaces.scan()
    # 获取扫描结果
    result = ifaces.scan_results()
    for name in result:
        # ssid WiFi名称
        print(name.ssid)


bies()
