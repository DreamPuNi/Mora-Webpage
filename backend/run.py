""" 这是main程序 """

import uvicorn
import logging
from app import create_app
from app.tasks.scheduler import start_scheduler

app = create_app()

if __name__ == "__main__":
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,  # 日志级别
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # 日志格式
        handlers=[
            logging.FileHandler("app.log", encoding="utf-8"),  # 写入文件
            logging.StreamHandler()  # 同时输出到控制台
        ]
    )

    start_scheduler()  # 启动定时任务
    uvicorn.run(app, host="127.0.0.1", port=8000)