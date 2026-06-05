
from django.urls import path,include
from . import views

urlpatterns = [
    # 列表页
    path('news_list/',views.news_list,name = 'news_list'),
    # 详情页
    path('list/<int:id>/',views.news_detail,name = 'news_detail'),
    # 案例列表页
    path('case_list/',views.case_list,name = 'case_list'),
    # 案例详情页
    path('case_list/<int:id>/',views.case_detail,name = 'case_detail'),
    
]