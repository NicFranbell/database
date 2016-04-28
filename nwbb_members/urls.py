from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'members'

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^view_members/$', views.view_members, name='view_members'),
    url(r'^add_user/$', views.add_user, name='add_user'),
    url(r'^edit_member_details/(?P<user_id>\d+)/$', views.edit_member_details, name='edit_member_details'),
    url(r'^view_member_details/(?P<user_id>\d+)/$', views.view_member_details, name='view_member_details'),
    url(r'^edit_user/(?P<user_id>\d+)/$', views.edit_user, name='edit_user'),
     url(r'^access_denied/', TemplateView.as_view(template_name="nwbb_members/access_denied.html")),
    url(r'^$', views.index, name='index'),
]