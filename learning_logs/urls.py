#定义learning_logs的url模式

from django.urls import path, include

from . import views
app_name = 'learning_logs'

urlpatterns = [
    #主页

    path('', views.index, name='index'),

    #显示所有的主题

    path('topics/',views.topics, name ='topics'),
    
    #显示特定主题的详细页面
    
    path('topics/(?P<topic_id>\d+)/',views.topic, name ='topic'),
    
    #用于添加新主题的网页
    path('new_topic/',views.new_topic, name = 'new_topic'),

    #用于添加新条目的页面
    path('new_entry/(?P<topic_id>\d+)/',views.new_entry, name = 'new_entry'),
    
]



