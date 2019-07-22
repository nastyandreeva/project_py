# -*- coding: utf-8 -*-
import os
import csv
import xlrd
lst1 = []


# Фун-ция по поиску файлов с расширением csv
def search_dir():
    dir_path = input("Введите абсолютный адрес: ")
    # Проверка пути на абсолютность
    if os.path.isabs(dir_path):
        for file in os.listdir(dir_path):
            if file.endswith(".csv"):
                lst1.append(os.path.join(dir_path, file))
        print(lst1)
    else:
        print("Введённый адрес не является абсолютным!")


search_dir()

# C:\Users\andre\Desktop\Project\csv

filename = lst1[0]

rb = xlrd.open_workbook('C:\Users\andre\Desktop\Project\csv\test.xls', formatting_info=True)
sheet = rb.sheet_by_index(0)

row = []
for i in range(sheet.nrows):
    r = sheet.row_values(i)
    row.append(r)
print (row)
