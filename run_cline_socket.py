# -*- coding: utf-8 -*-

import socket, sqlite3, time, requests
from log import logger


def get_config():
    conn = sqlite3.connect('./data.sqlite')
    c = conn.cursor()
    cursor = c.execute('SELECT IP_address, IP_port FROM "config" WHERE is_use = 1')
    data = [[i for i in row] for row in cursor]
    IP_address = data[0][0]
    IP_port = int( data[0][1])

    #logger.info(f"获取配置信息， socket 请求地址：{IP_address}:{IP_port}")
    conn.close()
    return IP_address, IP_port


def socket_cline():
    ip_address, ip_port = get_config()

    # print(ip_address, ip_port)

    with socket.socket() as s:
        s.settimeout(100)
        s.connect(
            (ip_address, ip_port)
        )
        # 一. 接受 socket 数据
        data = s.recv(4096)
        data = data.decode(encoding="utf-8")  # '#13@2@12@1!   #13@2@12@1!' => {}
    if data:
        logger.info(f"收到数据：{data}")

    elif not data:
        logger.info("没有数据")
        return

    _d = data.split('@')

    k1 = _d[0][1:]
    k2 = _d[1]
    k3 = _d[2]
    k4 = _d[3][:-1]

    url = f'http://127.0.0.1/csv/{k1}/{k2}/{k3}/{k4}'
    resp = requests.get(url=url)
    resp = resp.content.decode('unicode_escape')
    logger.info(f"socket 请求web结果 {resp}")


def run_cline_socket(F=False):
    print(" socket进程 -------------- 启动", )
    while True:
        time.sleep(1)

        try:
            socket_cline()
            logger.info("连接socket成功")
        except BaseException as e:
            # logger.info(e)
            pass
        if F:
            break
