from django.conf import settings
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# 注册界面
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 注册后自动登录
            return redirect(settings.LOGIN_REDIRECT_URL)  # 跳转到主页
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# 登陆界面，并在登陆后跳转
class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

# 用户信息页面
@login_required
def profile(request):
    return render(request, 'profile.html' ,{'user': request.user})

# 提供一个用户状态 API（前端动态展示用户信息时需要）
@login_required
def get_user_info(request):
    user = request.user
    return JsonResponse({
        'username': user.username,
        'email': user.email,
        'is_superuser': user.is_superuser,
        'is_staff': user.is_staff,
        'is_active': user.is_active
    })