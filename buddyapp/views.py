# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from buddyapp.forms import UploadRouteForm, UserForm, UserProfileForm
import gpxpy
import gpxpy.gpx

@login_required
def index(request):
    context = RequestContext(request)
    return render_to_response('buddyapp/home.html', context)

@login_required
def my_routes(request):
    context = RequestContext(request)
    return render_to_response('buddyapp/my_routes.html')

@login_required
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

@login_required
#Adds a comment to the playlist page desired
def add_comment(request, route_name_slug):
    route = Route.objects.get(slug=route_name_slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author=request.user.username
            comment.route = route
            comment.save()
            return show_playlist(request, route_name_slug)
    else:
        form = CommentForm()
    return render(request, 'buddyapp/add_comment.html', {'form': form})


@login_required
#Adds a rating to the playlist page desired
def add_rating(request, route_name_slug):
    route = Route.objects.get(slug=route_name_slug)
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.author=request.user.username
            rating.route = route
            rating.save()
            return show_route(request, route_name_slug)
    else:
        form = RatingForm()
    return render(request, 'buddyapp/add_rating.html', {'form': form})

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
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response('buddyapp/register.html',
                             {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
                              context)


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/buddyapp/home.html')
            else:
                return HttpResponse("Your BikeBuddy account is disabled")
        else:
            print "Invalid login details: {0}. {1}".format(username, password)
            return HttpResponse("Invalid login details supplied")
    else:
        return render_to_response('registration/login.html', {}, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/buddyapp/login/')
