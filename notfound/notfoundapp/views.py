from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

courses=[
    {"id":1, "search":"python"},
    {"id":2, "search":"c"},
    {"id":3, "search":"c++"},
    {"id":4, "search":"c#"}
]

def courses_list(request):
    id=request.GET.get('id','0')
    for item in courses:  
        if item['id'] in courses:
            return render(request,'notfoundapp/joz.html')
        else :
            return render(request,'notfoundapp/not.html')


def courses2(request,search):
    data={}
    for item in courses:
        if item['search']=="py":
            data['course']=item
            return render(request,'notfoundapp/joz.html')
        else:
            return render(request,'notfoundapp/not.html',context=data)
        
