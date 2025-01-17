from django_q.tasks import schedule
from datetime import time, timedelta, datetime

# 定时任务
def update_currency_rate_task():
    from .services.rate import get_USDCNY_exrate_from_web
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")
    get_USDCNY_exrate_from_web(formatted_date, formatted_date)  # 更新为当前日期
