# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    context = RequestContext(request)
    return render_to_response('buddyapp/base.html', context)

def top_rated(request):
    route_list = Route.objects.order_by("-rating")[:40]
    context_dict = {'routes': route_list}
    response = render(request, 'bikebuddy/top_rated.html', context=context_dict)
    return response

def most_viewed(request):
    route_list = Route.objects.order_by("views")[:40]
    context_dict = {'route': route_list}
    response = render(request, 'bikeBuddy/most_viewed.html', context=context_dict)
    return response

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