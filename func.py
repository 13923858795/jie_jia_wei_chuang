from openpyxl import load_workbook


def execl_info(path):
    excel=load_workbook(path)
    sheet = excel.active  #通过表名获取

    data = []

    for i in sheet:

        _d = []
        for c in i:

            _d.append(c.value)

        data.append(_d)


    return data


path_name = "CN_通讯录.xlsx"
path_report = "Daily Report （收集结果）.xlsx"

datas = execl_info(path_name)

names = [i[0].strip() if i[0] else i[0] for i in datas[1:]]
report = execl_info(path_report)
report = [i[0].strip() if i[0] else i[0] for i in report[1:]]

for name in names:
    if name not in report:
        print(name)



