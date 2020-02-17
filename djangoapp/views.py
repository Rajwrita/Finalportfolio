from django.shortcuts import render,redirect
from django.http import HttpResponse
from djangoapp.models import Details
from djangoapp.form import DetailForm

# Create your views here.

def det(request):
    if request.method=="POST":
        form=DetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contacts/')
            
    else:
        form=DetailForm()
        return render(request,"contacts.html")

def about(request):
    return render(request,"about.html")

def meraki(request):
    return render(request,"meraki.html")
    
def blogs(request):
    return render(request,"blogs.html")