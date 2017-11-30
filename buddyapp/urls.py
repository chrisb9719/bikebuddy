from django.conf.urls import patterns,include, url
from buddyapp import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^my_routes/$', views.my_routes, name='my_routes'),
    url(r'^add_route/$', views.add_route, name='add_route'),
    url(r'^restriced/$', views.restricted, name='restricted'),

)
