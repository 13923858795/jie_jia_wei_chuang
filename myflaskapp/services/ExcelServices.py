import datetime as dt, os
from openpyxl import Workbook
from openpyxl import load_workbook
from myflaskapp.services.CsvServices import CsvServices
from myflaskapp.services.tools import address, ALPHABET


class ExcelServices:
    """对excel的所有操作 放在此处"""
    def __init__(self, k1, k2, k3, k4):
        """
        x y z 为传入的 官号 舟号 温区号


        1 获取 csv  数据
        2 初始化 excel
            1： 未创建的话  就新建一个excel
        3 写入
        """

        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4

        """ 1 获取 csv  数据"""
        self.csv = CsvServices()
        self.CONFIG = self.csv.CONFIG
        """初始化 excel"""
        self.FilePath = self.excel_init()
        """ 开始填写 """
        self.edit_excel()

    def excel_init(self):
        """
        本客户要求生成txt 文件 所以下文的execl 都会改成txt

        1 获取 当前应该使用的excel名
            如果不存在 则创建新的excel
        """
        file_path = self.CONFIG.Excel_output
        point = self.csv.info["point"]
        point_len = len(point)

        point_str = ""
        for i in range(point_len):
            point_str = point_str + f"P{i+1} "

        """如果不存在 则创建新的excel"""
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(f"Date	ToolID	TubeID	ZoneID	BoatID {point_str}\n")

        return file_path

    def edit_excel(self):

        csv = self.csv.info

        if not csv:
            return []

        info = [csv["time"], self.k1, self.k2, self.k3, self.k4] + [str(i) for i in csv['point']]

        info = ",".join(info)

        with open(self.FilePath, "a") as f:
            f.write(f"{info}\n")






