from django.conf.urls import url

from . import views

app_name = 'members'

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^view_members/$', views.view_members, name='view_members'),
    url(r'^$', views.index, name='index'),
]


