from users.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('avatar',)}),  # 加入自定义字段
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('avatar',)}),
    )

from django.contrib import admin
from api.models import CurrencyRate, Images, Books

# 注册 CurrencyRate
@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ('date', 'rate')  # 显示字段
    search_fields = ('date',)  # 搜索字段
    list_filter = ('date',)  # 过滤器

# 注册 Images
@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_folder', 'introduce')  # 显示字段
    search_fields = ('title', 'introduce')  # 搜索字段
    list_filter = ('upload_folder',)  # 过滤器

# 注册 Books
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'tag')  # 显示字段
    search_fields = ('title', 'author', 'tag')  # 搜索字段
    list_filter = ('tag',)  # 过滤器
