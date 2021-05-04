from django.shortcuts import render
from django.http import HttpResponse
import requests,json
from django.template import loader

# Create your views here.
def index(request):

	print('yes')
	template = loader.get_template('slots/landing_page.html')


	return HttpResponse(template.render({}, request))