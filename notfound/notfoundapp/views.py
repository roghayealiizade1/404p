from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

courses=[
    {"id":"python"},
    {"id":"c"},
    {"id":"c++"},
    {"id":"c#"}
]

def courses_list(request):
    for item in courses:
        if item in courses:
            return render(request,'joz.html')
        else :
            return render(request,'not.html')
        