# -*- coding: utf-8 -*-
import os
import csv
import pandas as pd
import codecs
import io

lst1 = []


# Фун-ция по поиску файлов с расширением csv
def search_dir():
    dir_path = input("Введите абсолютный адрес: ")
    # Проверка пути на абсолютность
    if os.path.isabs(dir_path):
        for file in os.listdir(dir_path):
            if file.endswith(".xls"):
                lst1.append(os.path.join(dir_path, file))
        print(lst1)
    else:
        print("Введённый адрес не является абсолютным!")


search_dir()

# C:\Users\andre\Desktop\Project\csv