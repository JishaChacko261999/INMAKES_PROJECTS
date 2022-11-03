from django.shortcuts import render
from django.http import HttpResponse
#Create your views here.
def demo(request):

  return  render(request,'index.html')
# def addition(requset):
#    num1=int(requset.GET['num1'])
#    num2 =int(requset.GET['num2'])
#    result=num1+num2
#    mul = num1 * num2
#    sub = num1 - num2
#    div= num1 / num2
#    return render(requset,'result.html',{'result':result,'mul':mul,'sub':sub,'div':div})
