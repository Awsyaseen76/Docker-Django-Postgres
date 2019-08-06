from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from auth_api.models import Auth


def test(request):
   text = Auth.objects.all()
   print(text)
   return HttpResponse(text)
