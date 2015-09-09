from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title><h1>Ridwan Arvihafiz Bakri</h1><h2>1206208050</h2></html>')