from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_pushpa(request):
    return HttpResponse('pushpa not a flower it is a fire')
