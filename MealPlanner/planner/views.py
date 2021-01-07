from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is where you can generate and plan meals for the week!")
