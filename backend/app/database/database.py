""" 这里封装了数据库操作方法 """

import os
import json
from app.config import Config


def read_json_file(file_name):
    """
    读取指定 JSON 文件的数据
    :param file_name: 文件名，只是文件名，不要路径
    :return: 文件的json数据
    """
    file_path = os.path.join(Config.ECONOMY_JSON, file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def write_json_file(file_name, data):
    """
    写入json数据到文件
    :param file_name: 文件名，只是文件名，不要路径
    :param data: 需要写入的数据，格式为str或者list
    :return: none
    """
    file_path = os.path.join(Config.ECONOMY_JSON, file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)