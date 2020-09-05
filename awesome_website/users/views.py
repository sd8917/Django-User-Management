from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.urls import reverse
from users.forms import  CustomerUserCreationsForm


# Create your views here.
def dashboard(request):
    return render(request, 'users/dashboard.html')

def register(request):
    if request.method=='GET':
        return render(request, "users/register.html",{"form" : CustomerUserCreationsForm})

    elif request.method=="POST":
        form = CustomerUserCreationsForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect(reverse("dashboard"))
            