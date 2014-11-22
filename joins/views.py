from django.shortcuts import render

from .forms import EmailForm

def home(request):
	print(request.POST["email"])
	form = EmailForm()
	context = {'form':form}
	template = "home.html"
	return render(request, template, context)

