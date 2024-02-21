'''定义users应用的URL模式'''
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # 包含默认的身份验证URL模式
    path('', include('django.contrib.auth.urls')),
]