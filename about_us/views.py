from django.shortcuts import render
from about_us.models import About_us,Partner
# Create your views here.
def about_us(request):

    dep_h = About_us.objects.all().order_by('-development_history_time')
    partner = Partner.objects.all()

    return render(request,'about_us.html',{'dep_h':dep_h,'partner':partner,})