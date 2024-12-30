""" 定时任务调度器 """

from apscheduler.schedulers.background import BackgroundScheduler
from app.services.get_economy_data import get_USDCNY_exrate_from_web
from app.models.currency_model import update_json_file
from datetime import datetime
import logging
import asyncio

logger = logging.getLogger(__name__)

def start_scheduler():
    """
    启动定时任务调度器。
    """
    scheduler = BackgroundScheduler()

    # 定时任务：每天凌晨 2 点更新汇率
    scheduler.add_job(update_USDCNY_exrate, "cron", hour=2, minute=0)

    scheduler.start()
    logging.info("Scheduler started.")


async def update_USDCNY_exrate():
    """
    定期爬取当天汇率数据并更新数据库。
    """
    try:
        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y-%m-%d")
        rate = await get_USDCNY_exrate_from_web(start_time=formatted_date, end_time=formatted_date)  # 调用爬取逻辑
        update_json_file(file_name="USDCNY_exrate.json",data=rate)  # 更新到数据库
        logging.info(f"Currency rate updated: {rate}")
    except Exception as e:
        logging.error(f"Failed to update currency data: {e}")

if __name__ == "__main__":
    asyncio.run(update_USDCNY_exrate())