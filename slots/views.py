from django.shortcuts import render
from django.http import HttpResponse
import requests,json
from django.template import loader
from datetime import datetime

# Create your views here.
def index(request):

	print(request.GET)

	pincode = request.GET['pincode']
	dt = request.GET['date']

	dt = datetime.strptime( dt , '%Y-%m-%d').strftime('%d-%m-%Y')
	print('dt', dt)
	res = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={dt}'.format(pincode=pincode, dt=dt))
	print('got the response', res.status_code)
	res = json.loads(res.text)


	print('got the response')

	template = loader.get_template('slots/index.html')
	print('got the tmpelate')
	context = {
		'centers': res['centers'],
	}
	print( res['centers'] )

	return HttpResponse(template.render(context, request))