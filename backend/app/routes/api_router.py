""" 又一层路由 """

from fastapi import APIRouter, HTTPException, Query
from app.services.get_economy_data import *
from app.database.database import read_json_file

router = APIRouter()

@router.get("/usdcny_rate", summary="获取美元对人民币的汇率")
async def fetch_currency_rate(
    start_time: str = Query(..., description="开始时间，格式为YYYY-MM-DD"),
    end_time: str = Query(..., description="结束时间，格式为YYYY-MM-DD")
):
    """
    获取美元兑人民币汇率
    获取方式 /api/usdcny_rate?start_time=2024-12-01&end_time=2024-12-25
    """
    try:
        rate = await get_USDCNY_exrate_from_json(start_time, end_time)
        return {"status": "success", "usd_to_cny": rate}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/books_info", summary="获取书籍相关信息")
async def fetch_books_info(
        tag: str = Query('all', description='筛选标签')
):
    """
    返回书籍的相关信息
    获取方式 /api/books
    :param tag:
    :return:
    """
    try:
        json_info = read_json_file("books_info.json")
        return json_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/imgs_info", summary="获取图片相关信息")
async def fetch_imgs_info():
    """
    返回图片的相关信息
    获取方式 /api/imgs_info
    :param:
    :return:
    """
    try:
        json_info = read_json_file("imgs_info.json")
        return json_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))