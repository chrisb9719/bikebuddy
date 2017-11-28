# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from buddyapp.forms import UploadRouteForm
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
<<<<<<< HEAD
            gpx = gpxpy.parse(gpx_file)
=======
        	#gpx = gpxpy.parse(gpx_file)
>>>>>>> 3158dea530c81c968a3c2853db8dfe01109aec35
            for route in gpx.routes:
                print 'Route:'
    	        for point in route.points:
                    print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)
            return HttpResponseRedirect('buddyapp/home.html')
    else:
        form = UploadRouteForm()
    return render(request, 'buddyapp/add_route.html', {'form': form})

"""
def home(request):
        context_dict = {}
        route_list = Route.objects.order_by("-views")[:1]
        for route in route_list:
                top_viewed=Route.objects.get(name=playlist.name)
	context_dict ['most_viewed']= top_viewed

	route_list = Route.objects.order_by("-rating")[:1]
        for route in route_list:
                top_rated=Route.objects.get(name=route.name)
	context_dict ['routes_ratings'] =  top_rated

	response = render(request, 'bikebuddy/home.html', context = context_dict)
	return response

def show_route(request):
"""
