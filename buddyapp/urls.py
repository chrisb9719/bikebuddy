from django.conf.urls import patterns, url
from buddyapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^my_routes/$', views.my_routes, name='my_routes'),
    url(r'^add_route/$', views.add_route, name='add_route'),
)
