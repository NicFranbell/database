

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from .models import Member



@login_required
def index(request):
    #will build in who can see but just to get it working
    latest_member_list = Member.objects.all()
    template = loader.get_template('nwbb_members/index.html')
    context = {
        'latest_member_list': latest_member_list,
    }
    return HttpResponse(template.render(context, request))
    
