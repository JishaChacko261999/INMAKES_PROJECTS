from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demo(request):
  return  render(request,'homepage.html')
def about(requset):
  return render(requset,'about.html')
def contact(requset):
  return render(requset,'contact.html')
def details(requset):
  return render(requset,'details.html')
def tk(requset):
  return render(requset,'tk.html')



