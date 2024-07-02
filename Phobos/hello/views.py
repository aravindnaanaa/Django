from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
 return render(request, "hello/index.html")

def naanaa(request):
 return HttpResponse("Hello, Naanaa! Welcome to the real world")

def greetings(request, name):
 return render(request, "hello/greet.html",{
  "name":name.capitalize()
 })