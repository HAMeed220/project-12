from django.shortcuts import render

# Create your views here.

def Hameed(request):
    d = {'name':'Hameed'}
    return render(request,'Hameed.html')

def Mahesh(request):
    d = {'name':'Mahesh'}
    return render(request,'Mahesh.html')