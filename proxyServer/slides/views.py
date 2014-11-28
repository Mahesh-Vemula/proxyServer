from django.shortcuts import render
from django.http import HttpResponse
from .models import cacheData
from django.utils.timezone import utc
import datetime
# Create your views here.

def next(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		print x_forwarded_for
		ip = x_forwarded_for.split(',')[-1].strip()
	else:
		#print request.META
		ip = request.META.get('REMOTE_ADDR')
	new = cacheData.objects.filter(ip_address = ip)
	if new:
		previous_time = new[0].updated
		now = datetime.datetime.utcnow().replace(tzinfo=utc)
		timeDifference = now - previous_time
		if timeDifference.total_seconds() < 60:
			x = new[0].present_slide
			new[0].present_slide += 1
			new[0].save()
		else:
			new[0].present_slide = 1
			new[0].save()
			x=1
	else:
		cacheData.objects.create(ip_address = ip, present_slide = 1)
		x = 1
	
	return HttpResponse("Hello, You are in slides home now and slide Number "+str(x))