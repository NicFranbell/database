

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Member



@login_required
def index(request):
    return render(request, 'nwbb_members/index.html', {'username':request.user.username})
    
@login_required
def view_members(request):
    return render(request, "nwbb_members/view_members.html", {'latest_member_list' : Member.objects.all()})