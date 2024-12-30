import os
import json
from app.config import Config
from app.database.database import *


def update_json_file(file_name, data):
    """
    将data的数据经去重后更新到file_name
    """
    raw_data = read_json_file(file_name)
    unique_data = {item["date"]: item for item in (data + raw_data)}
    merged_data = list(unique_data.values())
    write_json_file(file_name, merged_data)

