from django.conf.urls import patterns, url
from buddyapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^my_routes/$', views.my_routes, name='my_routes'),
    url(r'^add_route/$', views.add_route, name='add_route'),
    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^regisiter/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
)
