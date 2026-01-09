#!/usr/bin/env python1
# -*- coding: utf-8 -*-
# @Time    : 2025/8/27 16:00
# @Author  : songyoukang
# @File    : read_yaml.py
# @Software: PyCharm
import os
import yaml

# def read_yaml(index,filename="login.yaml"):
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(current_dir, "..", "data", filename)
#     print(f"YAML文件路径: {file_path}")
#
#     test_data = []
#     try:
#         with open(file_path, 'r', encoding='utf-8') as f:
#             yaml_data = yaml.safe_load(f)
#             # 获取列表（如 data_list），再通过索引取数据
#             data_list = yaml_data.get("data_list", [])
#             # 判断索引是否有效
#             if 0 <= index < len(data_list):
#                 return data_list[index]
#             else:
#                 print(f"索引 {index} 超出范围（共{len(data_list)}条数据）")
#                 return None
#     except Exception as e:
#         print(f"读取失败: {e}")
#         return None
#
# if __name__ == '__main__':
#     data = read_yaml(1)
#     print("读取到的测试数据:", data)
#定义函数
import yaml
import os

from config import BASE_PATH


def read_yaml(filename):
    file_path = BASE_PATH + os.sep + 'data' + os.sep + filename
    print(f"YAML文件路径: {file_path}")
    #定义空列表，组装测试数据
    arr=[]
    #获取文件流
    with open(file_path,'r',encoding='utf-8') as f:
        for datas in yaml.safe_load(f).values():
          arr.append(tuple(datas.values()))
    return arr
if __name__ == '__main__':
    print(read_yaml("login.yaml"))



