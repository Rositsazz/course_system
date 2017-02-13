from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy

from .models import User
from .decorators import login_required
from .helpers import (factorial, fibonacci, first_N_primes)

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


def login(request):
    session_email = request.session.get('email', False)

    if session_email:
        return redirect(reverse('profile'))

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        u = User.login(email, password)

        if u is None:
            error = 'Wrong username/password'
        else:
            request.session['email'] = email
            return redirect(reverse('website:profile'))

    return render(request, 'website/login.html', locals())


@login_required(redirect_url=reverse_lazy('login'))
def home(request):
    if request.method == 'POST':
        if request.POST.get('delete_session', False):
            session_key = request.POST.get('session_key')
            if session_key in request.session:
                del request.session[session_key]
        else:
            session_key = request.POST.get('session_key')
            session_value = request.POST.get('session_value')

            request.session[session_key] = session_value

    return render(request, 'website/index.html', locals())


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
