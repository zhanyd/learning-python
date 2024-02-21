'''定义learning_logs应用的URL模式'''
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有的主题
    path('topics/', views.topics, name='topics'),
    # 显示主题的详细信息
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 添加新主题
    path('new_topic/', views.new_topic, name='new_topic'),
    # 添加新条目
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 编辑条目
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]