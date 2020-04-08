import time


def timestamp(time_str):
    return int(time.mktime(time.strptime(time_str, "%Y/%m/%d %H:%M:%S")))


ALPHABET = [chr(i) for i in range(65, 91)] + ["AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH"] # 字母表


def address(x, y):
    return f'{ALPHABET[y-1]}{x}'
