from django.shortcuts import render

from .forms import EmailForm, JoinForm
from .models import Join
from uuid import uuid4

def get_ip(request):
	try:
		x_foward = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get('REMOTE_ADDR')
	except:
		ip = ""

	return ip

def get_ref_id():
	return str(uuid4())[:11].replace('-','').lower()

def home(request, debug=False):
	if debug == True:
		print(request)
		
	# Bad way
	# form = EmailForm(request.POST)
	# if form.is_valid():
	# 	email = form.cleaned_data['email']
	# 	new_join, created = Join.objects.get_or_create(email=email)
	# 	print(new_join, created)
	# 	print(new_join.timestamp)
	# 	if created:
	# 		print("This object was created.")

	# Good way
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		new_join.ref_id = get_ref_id()
		new_join.ip_address = get_ip(request)
		new_join.save()

	context = {'form':form}
	template = "home.html"
	return render(request, template, context)

