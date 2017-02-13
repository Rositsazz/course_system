from django.shortcuts import render, redirect
from .helpers import (factorial, fibonacci, first_N_primes)


from .models import User
from django.core.urlresolvers import reverse, reverse_lazy

# from .decorators import login_required


def register(request):
    if request.method == 'POST':

        email = request.POST['email']
        # email = request.POST.get("email")
        password = request.POST['password']

        if not User.exists(email):
            user = User(email=email, password=password)
            user.save()
        else:
            error = 'User already exists'

    return render(request, 'website/register.html', locals())


def index(request):
    return render(request, "website/index.html", locals())


def fact(request):
    if request.method == "POST":
        number = int(request.POST.get("number"))
        fact_number = factorial(number)
    return render(request, "website/index.html", locals())


def fib(request):
    if request.method == "POST":
        number = int(request.POST.get("number"))
        fib_number = fibonacci(number)
    return render(request, "website/index.html", locals())


def prime(request):
    if request.method == "POST":
        number = int(request.POST.get("number"))
        primes = first_N_primes(number)
    return render(request, "website/index.html", locals())
