from email import message
from unicodedata import name
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
import getpass
import cgi
import cgitb


# Create your views here.
def  home(request):
    return render(request,"authentication/index.html")

def superadmin(request):
    return render(request, "authentication/superadmin.html")

def admin(request):
    form = cgi.FieldStorage()
    username=form.getvalue('username')
    pass0=form.getvalue('pass0')
    a = "shalik"
    b = "2804"
    if username== a and pass0==b:
        return redirect('lastpage') 
    return render(request, "authentication/admin.html")


def lastpage(request):
    return render(request, "authentication/lastpage.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        destination = request.POST['destination']
        email = request.POST['email']       
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.name=name
        myuser.destination=destination

        myuser.save()
        messages.success(request,"Your accout has been succesfully created.")

        return redirect('signin')



    return render(request, "authentication/signup.html")

def signinA(request):
    form = cgi.FieldStorage()
    username=form.getvalue('username')
    pass0=form.getvalue('pass0')
    a = "shalik"
    b = "2804"
    if username== a and pass0==b:
        return redirect('lastpage') 
    return render(request, "authentication/signinA.html")
    
def signin(request):

    if request.method == 'POST':
        username = request.POST['username']     
        pass1 = request.POST['pass1']

        user = authenticate(username= username, password= pass1)

        if user is not None:
            login(request, user)
            name=user.first_name
            return render (request, "authentication/lastpage.html", { 'name' :name} )

        else:
            message.error(request, "Bad Credentials!")
            return redirect('home')
    return render(request, "authentication/signin.html")
