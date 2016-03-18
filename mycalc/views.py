from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse(" <h1>Calculadora Django <h1>")
def add(request,num1,num2):
    suma=int(num1)+int(num2)
    return HttpResponse(" Suma : "+"<strong>"+str(num1)+" + "+str(num2)+" = "+str(suma))

def subs(request,num1,num2):
    rest=int(num1)-int(num2)
    return HttpResponse(" Resta : "+"<strong>"+str(num1)+" - "+str(num2)+" = "+str(rest))

def mult(request,num1,num2):
    mult=int(num1)*int(num2)
    return HttpResponse(" Multiplicacion : "+"<strong>"+str(num1)+" * "+str(num2)+" = "+str(mult))

def div(request,num1,num2):
    div=int(num1)/int(num2)
    return HttpResponse(" Division : "+"<strong>"+str(num1)+" / "+str(num2)+" = "+str(div))

def error (request):
    return HttpResponse(" <h1>Not Found <h1>")
