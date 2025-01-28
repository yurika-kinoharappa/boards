from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login:login")
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})



def study(request):
    return HttpResponseRedirect(reverse("event:study"))


def diary(request):
    return HttpResponseRedirect(reverse("event:diary"))


def dd(request):
    return HttpResponseRedirect(reverse("event:dd"))


def diet(request):
    return HttpResponseRedirect(reverse("event:diet"))


def smoke(request):
    return HttpResponseRedirect(reverse("event:smoke"))