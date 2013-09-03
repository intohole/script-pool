#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import socket
import fcntl
import struct

'''
功能:获得本机ｉｐ地址
原理:
参数: 1 . ifname 网卡名称 eth0
返回: sting  ip地址(本机)
'''
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

