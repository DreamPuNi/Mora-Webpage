import os
from pathlib import Path
from django.conf.global_settings import STATICFILES_DIRS

# 定义项目的根目录
BASE_DIR = Path(__file__).resolve().parent.parent

# 项目使用的密钥，用于加密。必须在生产环境中保密。
SECRET_KEY = 'django-insecure-+l%ie!_7$md44f2zm^i+2%z0)$h%t#0q%0r9ekmvv0*72l9z4x'

# Debug开关
DEBUG = True

# 定义允许访问此项目的主机名（例如：localhost、域名）。空列表表示只允许本地访问。
ALLOWED_HOSTS = []

# 配置媒体保存目录
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Django-Q定时任务设置
Q_CLUSTER = {
    'name': 'DjangoQ',
    'workers': 4,
    'timeout': 60,
    'retry': 120,
    'django_redis': 'default',
}

# 配置默认数据库为 SQLite3，数据库文件存储在项目根目录下。
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 应用定义
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'rest_framework',
    'users',
    'corsheaders',
]

# 允许启用凭证
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
# 允许来自 localhost:3000 的请求
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]
# 允许本地CSRF
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:5500',  # 添加你的前端地址
]


# 中间件：处理请求和响应的组件链。
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

# 项目 URL 配置的根模块。Django 将从这里加载 URL 路由规则。
ROOT_URLCONF = 'mora_backend.urls'

# 配置模板路径和静态文件路径
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'static'/ 'html'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 配置静态文件（CSS、JS、图片等）的 URL 前缀。
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# 登出跳转地址
LOGIN_REDIRECT_URL = 'http://127.0.0.1:5500/index.html'
LOGOUT_REDIRECT_URL = 'http://127.0.0.1:5500/index.html'

# 配置用户模型数据库
AUTH_USER_MODEL = 'users.User'

# 配置项目的 WSGI（Web服务器网关接口）应用，负责处理 HTTP 请求。
WSGI_APPLICATION = 'mora_backend.wsgi.application'

# 配置用户密码的验证规则，例如最低长度要求、避免使用常见密码等。
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# 配置语言、时区以及是否启用国际化（I18N）和时区支持（TZ）
USE_TZ = True
USE_I18N = True
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'zh-hans'
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

# 配置模型的默认主键字段类型为 BigAutoField。
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

