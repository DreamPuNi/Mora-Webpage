from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 自定义字段
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)  # 可选头像

    def __str__(self):
        return self.username  # 使用用户名作为字符串表示
