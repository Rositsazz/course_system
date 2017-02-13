from django.shortcuts import render
from .helpers import (factorial, fibonacci, first_N_primes)


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
