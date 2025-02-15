from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse("home"))

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect(reverse("login"))
    else:
        form = RegisterForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/register.html", context)


@login_required
def logout_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse("login"))

    if request.method == "POST":
        logout(request)
        return redirect(reverse("login"))
    return redirect(reverse("home"))
