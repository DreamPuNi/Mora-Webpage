# How To 部署

设置json数据库文件夹位置：```export JSON_FOLDER="/absolute/path/to/data/json_files"```
selenium使用的是Edge浏览器，需要修改请去```app/services/get_economy_data.py```

# 使用方法

## API列表

获取人民币美元汇率

```
/api/currency?start_time=2024-12-01&end_time=2024-12-25
```

输出

```json
{
    "status": "success",
    "usd_to_cny": [
        {"date": "2024-12-24","rate": "7.3178"},
        {"date": "2024-12-23","rate": "7.3178"},
        {"date": "2024-12-22","rate": "7.3168"}
    ]
}
```