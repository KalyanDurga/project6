from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def dhoni(request):
    return HttpResponse('<h1><marquee>MS Dhoni is the best captian and best All Rounder</marquee></h1>')


def bravo(request):
    return HttpResponse('<h1><marquee>DJ Bravooo DJ bravooo Champion The Champion</marquee></h1>')
