# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from buddyapp.forms import UploadRouteForm, UserForm, UserProfileForm
import gpxpy
import gpxpy.gpx

def index(request):
    context = RequestContext(request)
    return render_to_response('buddyapp/home.html', context)

def my_routes(request):
    context = RequestContext(request)
    return render_to_response('buddyapp/my_routes.html')

def add_route(request):
    if request.method == 'POST':
        form = UploadRouteForm(request.POST, request.FILES)
        if form.is_valid():
            gpx_file = open(form.name, 'r')
            gpx = gpxpy.parse(gpx_file)
            for route in gpx.routes:
                print 'Route:'
    	        for point in route.points:
                    print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)
            return HttpResponseRedirect('buddyapp/home.html')
    else:
        form = UploadRouteForm()
    return render(request, 'buddyapp/add_route.html', {'form': form})

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save()
            profile.user = user
            profile.save()
            registered=True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render_to_response('registration/registration_form.html',
                             {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
                              context)
