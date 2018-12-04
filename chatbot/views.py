from django.shortcuts import render
from django.views import generic

# Create your views here.
from django.http.response import HttpResponse


def bview(request):
    return HttpResponse("Hello World")


class botview(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World!")
