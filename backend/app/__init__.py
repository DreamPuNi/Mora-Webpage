""" 这里是api路由注册 """

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.api_router import router as currency_router

def create_app():
    app = FastAPI(
        title="Currency Exchange API",
        description="获取美元兑人民币汇率",
        version="1.0.0"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://127.0.0.1:5500"],  # 允许的前端来源
        allow_credentials=True,                  # 允许传递 Cookies
        allow_methods=["*"],                     # 允许的 HTTP 方法
        allow_headers=["*"],                     # 允许的 HTTP 头
    )

    # 注册路由
    app.include_router(currency_router, prefix="/api")
    return app
