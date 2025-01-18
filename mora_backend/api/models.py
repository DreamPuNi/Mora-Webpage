import os
from django.db import models

# 动态生成img文件夹路径
def upload_to_dynamic(instance, filename):
    base_folder = 'images'
    sub_folder = getattr(instance, 'upload_folder', 'default')  # 默认文件夹
    return os.path.join(base_folder, sub_folder, filename)

# 汇率管理
class CurrencyRate(models.Model):
    date = models.DateField(unique=True)  # 日期（唯一值）
    rate = models.DecimalField(max_digits=10, decimal_places=4)  # 汇率值
    def __str__(self):
        return f"{self.date}: {self.rate}"

# 图片上传管理
class Images(models.Model):
    title = models.CharField(max_length=255)
    data = models.ImageField(upload_to=upload_to_dynamic)  # 动态文件夹路径
    introduce = models.TextField()
    upload_folder = models.CharField(max_length=255, default='xinpo')  # 存储文件夹名称
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'Images'

# 书籍信息上传管理
class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='images/books-cover')  # 书籍封面路径
    description = models.TextField()
    review = models.TextField()
    link = models.URLField()
    tag = models.CharField(max_length=50)
    class Meta:
        db_table = 'Books'  # 指定表名

# 智典数据管理
class Chapter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    parent = models.ForeignKey(
        'self', null=True,blank=True,on_delete=models.CASCADE,related_name='sub_chapters'
    )
    # 告诉Python，当需要以字符串形式表示一个Chapter实例时，应该返回title字段的值。
    def __str__(self):
        return self.title

''' 这部分是定义模型，然后数据库会根据模型生成数据库表

运行以下命令将模型同步到数据库：
python manage.py makemigrations
python manage.py migrate

写数据（保存到数据库）：
CurrencyRate.objects.create(date="2025-01-05", rate=7.1234)

读数据（从数据库查询）：
rate = CurrencyRate.objects.get(date="2025-01-05")
print(rate.rate)  # 输出 7.1234

更新数据：
rate = CurrencyRate.objects.get(date="2025-01-05")
rate.rate = 7.2345
rate.save()

删除数据：
rate = CurrencyRate.objects.get(date="2025-01-05")
rate.delete()
'''