import os, csv, json
from myflaskapp.services.ConfigServices import ConfigServices


class CsvServices:
    def __init__(self):
        """
        1: 获得配置信息
        2： 获取最新的 csv文件 并对其进行解析
        3: 写入 excel
        """
        self.CONFIG = ConfigServices.get_model()  # 1: 获得配置信息
        self.info = self.csv_analysis()  # 2： 获取最新的 csv文件 并对其进行解析

    def csv_analysis(self):
        """获取最新一个csv文件"""
        file = []
        for i in os.listdir(self.CONFIG.CSV_file):
            if 'CSV' not in i:
                continue
            file.append(i)

        file.sort(key=lambda x: int(x[:-4]))
        if not file:
            return []
        file = file[-1]
        csv_path = self.CONFIG.CSV_file + f'\\{file}'

        csv_data = []
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                csv_data.append(row)

        """  主要获取参数 1: 创建时间   2： 对应栏位点数   """
        resp = {}
        resp["time"] = csv_data[0][1]
        resp["RES_JUDGMENT"] = None
        TestPoint = [int(i) for i in self.CONFIG.TestPoint.split(",")]  # 要采样的点位
        CSV_data = int(self.CONFIG.CSV_data)  # 数据栏位

        points = []
        for _d in csv_data:
            _k = _d[0]
            if _k == 'POINT':
                p_id = int(_d[1])
                if p_id not in TestPoint:  # 忽略不采样的点
                    _v = '/'
                else:
                    _v = float(_d[CSV_data - 1])
                points.append(_v)
            if _k == 'RES_JUDGMENT':
                resp["RES_JUDGMENT"] = _d[1]

        resp["point"] = points
        return resp
