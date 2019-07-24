# -*- coding: utf-8 -*-
import os
import xlrd
import json
lst1 = []
from class_model import *


# Фун-ция по поиску файлов с расширением xls
def search_dir(dir_path=None):
    # Проверка существования переданного пути
    if os.path.exists(dir_path):
        dir_path = dir_path if not None else input("Введите абсолютный адрес: ")
        # Проверка пути на абсолютность
        if os.path.isabs(dir_path):
            for file in os.listdir(dir_path):
                if file.endswith(".xls"):
                    lst1.append(os.path.join(dir_path, file))
            print(lst1)
        else:
            print("Введённый адрес не является абсолютным!")
    else:
        raise Exception("Заданный путь не существует")


search_dir('C:\\Users\\anastasiya.andreeva\\Desktop\\Project')

# C:\Users\anastasiya.andreeva\Desktop\Project

filename = lst1[0]

rb = xlrd.open_workbook(filename)
sheet = rb.sheet_by_index(0)

row = []
ModelParamCollection = []
for i in range(sheet.nrows):
    r = sheet.row_values(i)
    obj = ModelParam()
    obj.setId(r[0])
    obj.setUniqueId(r[1])
    obj.setNavisworks(r[2])
    obj.setLevel(r[3])
    obj.setSection(r[4])
    obj.setCategory(r[5])
    obj.setType(r[6])
    obj.setName(r[7])
    obj.setLength(r[8])
    obj.setSquare(r[9])
    obj.setVolume(r[10])
    obj.setOffset(r[11])
    obj.setOffsetUp(r[12])
    obj.setWidth(r[13])
    obj.setHeight(r[14])
    ModelParamCollection.append(obj)
"""
csv = []
for i in ModelParamCollection:
    csv.append(';'.join(list(map(lambda x: str(x), i.toList()))))
print("\n".join(csv))
"""

n = []
for i in ModelParamCollection:
    n.append(i.toDict())
#print(n)

json_string = json.dumps(n, sort_keys=False, indent=2, separators=(',', ': '), ensure_ascii=False)
print(json_string)

