from django.shortcuts import render

# Create your views here.

def landing(request):
	return render(request,'demo/home.html')

def about(request):
	return render(request,'demo/about.html')

def credits(request):
	return render(request,'demo/credits.html')