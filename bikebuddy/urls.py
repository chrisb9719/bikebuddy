from django.conf.urls import patterns, include, url
from buddyapp import views
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bikebuddy.views.home', name='home'),
    # url(r'^bikebuddy/', include('bikebuddy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^buddyapp/', include('buddyapp.urls')),
	url(r'^$', views.index, name = 'index'),
    url(r'^home/$', views.index, name='index'),
    url(r'^my_routes/$', views.my_routes, name='my_routes'),
    url(r'^add_route/$', views.add_route, name='add_route'),
    url(r'^registration/regisitration_form/$', views.register, name='register'),
    url(r'^registration/login/$', views.user_login, name='login'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^route/(?P<route_name_slug>[\w\-]+)/$', views.show_route, name='show_route'),
    #url(r'^my_routes/$', views.my_routes, name='my_routes'),
    #url(r'^home/accounts/password_change/$', auth_views.password_change, name='password_change'),
    #url(r'^accounts/password_change/$', auth_views.password_change, name='password_change'),
    #url(r'^accounts/password_change/done/$', auth_views.password_change_done, name='password_change_done'),
    #url(r'^view_all_routes/$', views.view_all_routes, name='view_all_routes'),
    #url(r'route/(?P<route_name_slug>[\w\-]+)/comment/$', views.add_comment_to_playlist, name='add_comment'),
    #url(r'route/(?P<route_name_slug>[\w\-]+)/rating/$', views.add_rating, name='add_rating'),
)
