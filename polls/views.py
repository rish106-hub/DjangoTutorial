from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    content="<html><body><h1>Welcome to Little Lemon</h1></body></html>"
    return HttpResponse(content)