""" 路由过来的函数 """

import json
import asyncio
from .models import *
from .serializers import ChapterSerializer
from .services.rate import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser


class ImagesUploadView(APIView):
    ''' 心魄页图片上传 '''
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        introduce = request.data.get('introduce')
        data = request.FILES.get('data')  # 上传的图片文件
        upload_folder = request.data.get('folder', 'xinpo')  # 文件夹名称，默认为 'xinpo'

        if not title or not data or not introduce:
            return Response({"error": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)

        image_instance = Images(title=title, introduce=introduce, data=data, upload_folder=upload_folder)
        image_instance.save()
        return Response({
            "message": "Hero saved successfully.",
            "data": {
                "title": image_instance.title,
                "introduce": image_instance.introduce,
                "file_path": image_instance.data.url
            }
        }, status=status.HTTP_201_CREATED)

class BooksUploadView(APIView):
    ''' 书籍页图片上传 '''
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        author = request.data.get('author')
        cover = request.FILES.get('cover')  # 上传的封面图片
        description = request.data.get('description')
        review = request.data.get('review')
        link = request.data.get('link')
        tag = request.data.get('tag')

        if not title or not cover or not description:
            return Response({"error": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)

        # 使用 books_db 数据库保存数据
        book = Books(
            title=title,
            author=author,
            cover=cover,
            description=description,
            review=review,
            link=link,
            tag=tag
        )
        book.save()
        return Response({
            "message": "Book saved successfully.",
            "data": {
                "title": book.title,
                "author": book.author,
                "cover": book.cover.url
            }
        }, status=status.HTTP_201_CREATED)

class ChapterListView(APIView):
    '''用视图处理获取章节数据的请求'''
    def get(self,request):
        chapters = Chapter.objects.filter(parent=None) # 查询数据库，获取一级标题
        serializer = ChapterSerializer(chapters, many=True) # 创建序列化器实例。查询集为chapters，包含多个对象，并转为JSON格式的列表
        return Response(serializer.data) # 将序列化后的数据（一个 Python 列表，包含多个字典）封装到 DRF 提供的 Response 对象中，返回给客户端。

# 模拟异步获取汇率的函数
@csrf_exempt
def fetch_currency_rate(request):
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')
    if not start_time or not end_time:
        return JsonResponse({"status": "error", "detail": "Missing parameters"}, status=400)
    try:
        rate = get_USDCNY_exrate_from_database(start_time, end_time)
        return JsonResponse({"status": "success", "usd_to_cny": rate})
    except Exception as e:
        return JsonResponse({"status": "error", "detail": str(e)}, status=500)

@csrf_exempt
def fetch_books_info(request):
    try:
        tag = request.GET.get('tag', None)
        if tag == 'all' or not tag:
            books = Books.objects.all()  # 获取所有书籍
        else:
            books = Books.objects.filter(tag=tag)
        books_info = []
        for book in books:
            book_info = {
                'title': book.title,
                'author': book.author,
                'cover': book.cover.url,
                'description': book.description,
                'review': book.review,
                'link': book.link,
                'tag': book.tag
            }
            books_info.append(book_info)
        return JsonResponse({'status': 'success', 'data': books_info})
    except Exception as e:
        # 处理数据库错误
        return JsonResponse({'status': 'error', 'detail': str(e)}, status=500)

@csrf_exempt
def fetch_imgs_info(request):
    try:
        # 从数据库中获取所有图片信息
        images_info = []
        images = Images.objects.filter(upload_folder='xinpo')  # 假设你需要筛选出 'xinpo' 文件夹下的图片
        for image in images:
            image_info = {
                'title': image.title,
                'introduce': image.introduce,
                'image_url': image.data.url  # 获取图片的 URL
            }
            images_info.append(image_info)
        # 返回成功响应和图片数据
        return JsonResponse({'status': 'success', 'data': images_info})

    except Exception as e:
        # 处理数据库错误
        return JsonResponse({'status': 'error', 'detail': str(e)}, status=500)
