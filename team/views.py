from django.shortcuts import render

from team.models import Team

# Create your views here.
def team_list(request):

    # team
    teams = Team.objects.all().order_by('rank')
    return render(request,'team_list.html',{'teams':teams})