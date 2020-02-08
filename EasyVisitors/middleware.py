from django.conf import settings
from .models import Visitor
from django.core.management import call_command

# Time after which a user is concidered a new user in (( seconds ))
try:
	VisitorAliveTime = settings.EASY_COUNTER_VISITOR_ALIVE_TIME
except:
	VisitorAliveTime = 300

# Paths to be ignored from counter concideration (( currentPath.startswith ))
try:
	ignoredPaths = settings.EASY_COUNTER_IGNORED_PATHS
except:
	ignoredPaths = ['/admin']

# Value to be set once the counter is reset, None signifies no reset
try:
	counterReset = settings.EASY_COUNTER_RESET
except:
	counterReset = None

class VisitorCounterMiddleware(object):
	def __init__(self, get_response):
		# Future Feature
		# call_command("makemigrations","EasyVisitors")
		# call_command("migrate","EasyVisitors")
		self.get_response = get_response
	def __call__(self, request):
		# print(request.META['HTTP_USER_AGENT']) ~~ FUTURE FEATURE ~~

		# counter is reset to the value counterReset if counterReset has any
		# value except None, no cookies are made or checked in this case
		if(counterReset != None):
			try:
				CounterObject = Visitor.objects.get(name='Total Visitors')
			except:
				CounterObject = Visitor(name='Total Visitors')
			CounterObject.counter = counterReset
			CounterObject.save()
			request.visitors = counterReset
			response = self.get_response(request)
			return response

		# Path of page requesting the middleware
		currPath = request.get_full_path()
		
		# If the current URL startswith a path in the ignoredPaths then this URL is not
		# concidered in changing the counter value
		for path in ignoredPaths:
			if(currPath.startswith(path)):
				response = self.get_response(request)
				return response
		
		# Object of Visitor class is created if it doesnot already exists, with a 
		# value of 1 and name -> Total Visitors
		try:
			CounterObject = Visitor.objects.get(name='Total Visitors')
		except:
			CounterObject = Visitor(name='Total Visitors')
		
		# Current value of visitor counter as integer
		totalVisitors = int(CounterObject.counter)

		# Extracting cookie from request
		VisitorCookie = request.COOKIES.get("Visitor")

		# If cookie already exists the that means that the user has already been counted
		# in the visitor else it is now countef
		if(not VisitorCookie):
			totalVisitors += 1
			CounterObject.counter = totalVisitors
			CounterObject.save()

		# -> visitors <- is the name by which the counter value can accesed in 
		# templates by calling {{ request.visitors }}
		request.visitors = totalVisitors
		response = self.get_response(request)

		# If the cookie doesnot already exist or is expired then a new cookie is created
		if(not VisitorCookie):
			response.set_cookie('Visitor', 'Alive', max_age=VisitorAliveTime)
		
		# Modified request that a view recieves
		return response