from django.shortcuts import render
from news.models import News

# Create your views here.
def news_list(request):

    news_list = News.objects.filter(category_id=1)
    return render(request,'news_list.html',{'news_list':news_list})

def news_detail(request,id):

    news_detail = News.objects.get(pk=id)
    return render(request,'news_detail.html',{'news_detail':news_detail})

def case_list(request):

    case_list = News.objects.filter(category_id=2).order_by('creat_at')
    return render(request,'case_list.html',{'case_list':case_list})

def case_detail(request,id):

    case_detail = News.objects.get(pk=id)
    return render(request,'case_detail.html',{'case_detail':case_detail})