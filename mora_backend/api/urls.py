from .views import ImagesUploadView, fetch_currency_rate
from django.urls import path
from . import views

urlpatterns = [
    path('usdcny_rate/', views.fetch_currency_rate, name='fetch_currency_rate'),
    path('books_info/', views.fetch_books_info, name='fetch_books_info'),
    path('upload_book/', views.BooksUploadView.as_view(), name='upload_books'),
    path('imgs_info/', views.fetch_imgs_info, name='fetch_imgs_info'),
    path('upload_images/', views.ImagesUploadView.as_view(), name='upload_images'),
]
