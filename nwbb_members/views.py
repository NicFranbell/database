

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from  .models import Member,MemberRole 
from nwbb_members.forms import MemberForm, UserForm
from database.tools import random_word
from database.utility import can_view_member, can_add_member

@login_required
def index(request):
    return render(request, 'nwbb_members/index.html', {'username':request.user.username})
    
@login_required
@user_passes_test(can_view_member, "/members/access_denied", None)
def view_members(request):
    return render(request, "nwbb_members/view_members.html", {'latest_member_list' : Member.objects.all()})

@login_required
@user_passes_test(can_view_member, "/members/access_denied", None)
def view_member_details(request, user_id):
    member = get_object_or_404(User, pk=user_id)
    response_dict = {'member': member} 
    response_dict['member_role'] = MemberRole.objects.filter(member=member)
    return render_to_response('nwbb_members/view_member_details.html', response_dict, context_instance=RequestContext(request))

@login_required
@user_passes_test(can_add_member,"/members/access_denied", None )
def edit_member_details(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    response_dict = {'member': user.profile}
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=user.profile)
        response_dict['form'] = form
        if form.is_valid():
            form.save()
            if 'return_url' in request.GET:
                return HttpResponseRedirect(request.GET['return_url'])
            else:
                return HttpResponseRedirect(reverse("members:view_member_details", kwargs={'user_id':user_id}))
    else:            
        form = MemberForm(instance=user.profile)
        response_dict['form'] = form
    return render_to_response('nwbb_members/edit_member_details.html', response_dict,
                             context_instance=RequestContext(request))
    
@login_required
@user_passes_test(can_add_member, "/members/access_denied", None)
def add_user(request):
    response_dict = {}
    if request.method == 'POST': 
        form = UserForm(request.POST)
        response_dict['form'] = form
        if form.is_valid():
            new_user = form.save()
            new_user.password = make_password(random_word(18))
            new_user.save()
            Member(user=new_user).save()
            return HttpResponseRedirect(reverse("members:edit_member_details", kwargs={'user_id':new_user.id}))
    else:
        form = UserForm()
        response_dict['form'] = form
    return render_to_response('nwbb_members/add_user.html', response_dict, context_instance=RequestContext(request))

@login_required
def edit_user(request, user_id):
    member = get_object_or_404(User, pk=user_id)
    response_dict = {'member': member}
    if request.method == 'POST':  # If the form has been submitted...
        form = UserForm(request.POST, request.FILES, instance=member.profile)  # A form bound to the POST
        response_dict['form'] = form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("members:view_member_details", args=(member.id)))
    else:
        form = UserForm(instance=member.profile)
        response_dict['form'] = form
    return render_to_response('nwbb_members/edit_user.html', response_dict, context_instance=RequestContext(request))

