from django.shortcuts import render, redirect
from django.contrib import messages
from .models import registration

# Create your views here.
def index(request):
    context = {
    "objects": registration.objects.all()
    }
    return render(request, "loginRegApp/index.html", context)

def validator(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    password = request.POST["password"]
    password2 = request.POST["password2"]

    validation = registration.objects.validator(first_name, last_name, email, password, password2)

    #If there were errors, runs through each shorthand error in errorlist (validation[1]), and then translates them to the longhand error
    #in errordict (validation[2]) and turns them into flash messages, then redirects to the homepage
    if not validation[0]:
        for error in validation[1]:
            messages.info(request, validation[2][error])
        return redirect ("/")

    request.session['id'] = validation[1]
    print request.session["id"]
    return redirect ("/success")

def login(request):
    password = request.POST["password"]
    email = request.POST["email"]

    login = registration.objects.login(email, password)

    if not login[0]:
        for error in login[1]:
            messages.info(request, login[2][error])
        return redirect ("/")
    request.session['id'] = login[1]
    print request.session["id"]
    return redirect("/success")

def success(request):
    if "id" not in request.session:
        messages.info(request, "Please log in to continue.")
        return redirect("/")

    context = {
    "selection" : registration.objects.get(id = request.session["id"]).first_name
    }
    return render(request, "loginRegApp/success.html", context)

def logout(request):
    request.session.pop("id")
    messages.info(request, "Thank you for logging out.  Goodbye!")
    return redirect("/")
