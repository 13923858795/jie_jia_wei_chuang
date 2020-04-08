# -*- coding: utf-8 -*-
import datetime as dt
import socket, sqlite3, time, requests
from log import logger



# def socket_cline():
#     # ip_address, ip_port = "192.168.1.16", 20000
#     ip_address, ip_port = "192.168.119.1", 10000
#     # print(ip_address, ip_port)
#
#     with socket.socket() as s:
#         s.settimeout(100)
#         s.connect(
#             (ip_address, ip_port)
#         )
#
#         print(f"链接成功: {dt.datetime.now()}")
#
#         # 一. 接受 socket 数据
#
#         while True:
#             data = s.recv(1024)
#             print(f"{dt.datetime.now()} 收到数据------------------------", data)
#             data = data.decode(encoding="utf-8")  # '#13@2@12@1!#13@2@12@1!' => {}
#             if data:
#                 print("收到数据------------------------", data)
#                 logger.info(f"收到数据：{data}")
#             break
#
#
# while True:
#     try:
#         socket_cline()
#     except BaseException as e:
#         print(f"错误时间：发{dt.datetime.now()}")


import requests

url = f'http://127.0.0.1/csv/1/2/3/4'
resp = requests.get(url=url)
resp = resp.content.decode('unicode_escape')
print(resp)