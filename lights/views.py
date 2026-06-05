
from django.http import HttpResponse
from django.shortcuts import render
from slide.models import Slide
from team.models import Team
from news.models import News,Category

# Create your views here.
def index(request):
    # slide
    slides = Slide.objects.all()
    # team
    teams = Team.objects.all().order_by('rank')
    # news
    news = News.objects.filter(category_id=1).order_by('-creat_at')[:3]
    # case
    news_case = News.objects.filter().exclude(category_id=1).order_by('-creat_at')

    return render(request,'index.html',{ 
        'slides':slides,
        'teams':teams,
        'news':news,
        'news_case':news_case,

        })

