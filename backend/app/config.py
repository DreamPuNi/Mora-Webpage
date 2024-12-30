""" 这里我放的是数据库的地址和相关信息 """

import os

class Config:
    ECONOMY_JSON = os.getenv("JSON_FOLDER", os.path.abspath(r"D:\Program\webpage\HermaeusMora\database\json"))