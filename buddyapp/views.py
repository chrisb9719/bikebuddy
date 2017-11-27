# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import gpxpy
import gpxpy.gpx

def index(request):
    context = RequestContext(request)
    return render_to_response('buddyapp/home.html', context)

def my_routes(request):
    context = RequestContext(request)
    return render_to_response('buddyapp/my_routes.html')

def add_route(request):
    context = RequestContext(request)
    return render_to_response('buddyapp/add_route.html')

"""def home(request):
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

# Parsing an existing file:
# -------------------------

	gpx_file = open('test_files/cerknicko-jezero.gpx', 'r')

	gpx = gpxpy.parse(gpx_file)

	for track in gpx.tracks:
		for segment in track.segments:
			for point in segment.points:
				print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)

	for waypoint in gpx.waypoints:
		print 'waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude)

	for route in gpx.routes:
		print 'Route:'
		for point in route.points:
			print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)

	# There are many more utility methods and functions:
	# You can manipulate/add/remove tracks, segments, points, waypoints and routes and
	# get the GPX XML file from the resulting object:

	print 'GPX:', gpx.to_xml()

	# Creating a new file:
	# --------------------

	gpx = gpxpy.gpx.GPX()

	# Create first track in our GPX:
	gpx_track = gpxpy.gpx.GPXTrack()
	gpx.tracks.append(gpx_track)

	# Create first segment in our GPX track:
	gpx_segment = gpxpy.gpx.GPXTrackSegment()
	gpx_track.segments.append(gpx_segment)

	# Create points:
	gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1234, 5.1234, elevation=1234))
	gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1235, 5.1235, elevation=1235))
	gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1236, 5.1236, elevation=1236))

	# You can add routes and waypoints, too...

	print 'Created GPX:', gpx.to_xml()
    """
