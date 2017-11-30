from django.conf.urls import patterns,include, url
from buddyapp import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name = 'index'),
    url(r'^my_routes/$', views.my_routes, name='my_routes'),
    url(r'^add_route/$', views.add_route, name='add_route'),

    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^regisiter/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),

    url(r'^restriced/$', views.restricted, name='restricted'),


)
