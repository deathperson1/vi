from django.shortcuts import render,HttpResponse
import requests

# Create your views here.

def vishal(request):
    return render(request,"home.html")


def countries(request):
    data=requests.get("https://restcountries.eu/rest/v2/all").json()
    return render(request,"all.html",{"con":data} )