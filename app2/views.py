from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return HttpResponse('<h1><marquee>Virat Kohili is the The King Of Cricket...</marquee></h1>')

def abd(request):
    return HttpResponse('<h2><marquee>ABD is Well Known As MR 360 The Legend</marquee></h1>')