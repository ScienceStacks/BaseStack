from django import forms
from django.http import HttpResponse


#######################
# Request handlers
#######################
def hello(request):
  return HttpResponse("Hello world")
