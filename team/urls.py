from django.urls import path,include
from . import views

urlpatterns = [
    # 列表页
    path('team_list/', views.team_list, name='team_list')
    
]