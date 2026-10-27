from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, DocumentForm


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

    return render(request, "accounts/login.html")


def user_logout(request):
    logout(request)
    return redirect("home")


@login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard/dashboard.html")


@login_required(login_url="login")
def upload_document(request):

    if request.method == "POST":

        print("=" * 50)
        print("POST Request Received")
        print("FILES :", request.FILES)
        print("=" * 50)

        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():

            print("FORM IS VALID")

            document = form.save(commit=False)
            document.user = request.user
            document.save()

            print("DOCUMENT SAVED SUCCESSFULLY")
            print("Title :", document.title)
            print("File  :", document.file.name)

            return redirect("dashboard")

        else:

            print("FORM IS NOT VALID")
            print(form.errors)

    else:

        form = DocumentForm()

    return render(
        request,
        "documents/upload.html",
        {
            "form": form
        }
    )