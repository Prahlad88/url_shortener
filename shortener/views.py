from urllib import request

from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import URLForm
from .models import ShortenerTable
from . import qr
import string
import random


def homepage(request):
    return render(request, 'homepage.html', {})


def generate_short_url():
    alphabet = string.digits + string.ascii_lowercase + string.ascii_uppercase
    random_base62 = ''.join(random.choice(alphabet) for _ in range(8))
    return random_base62


def is_unique(short_url):
    return not ShortenerTable.objects.filter(short_url=short_url).exists()


def get_unique_short_url():
    while True:
        unique_id = generate_short_url()
        short_url = f"http://127.0.0.1:8000/s/{unique_id}"
        if is_unique(short_url):
            return short_url


def shorten_url(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            username = request.user.username
            form = URLForm(request.POST)
            if form.is_valid():
                original_url = form.cleaned_data['original_url']

                short_url = get_unique_short_url()
                qr_code = qr.generate_qr_code(short_url)

                url = ShortenerTable(original_url=original_url, short_url=short_url,
                                     qr_code=qr_code, created_by=username)

                url.save()
                response_data = {'short_url': url.short_url, 'qr_encoded': url.qr_code}
                return JsonResponse(response_data)
            else:
                errors = form.errors.as_json()
                return JsonResponse({'error': errors}, status=400)


def find_long_url(request, short_url):
    try:
        short_url = f"http://127.0.0.1:8000/s/{short_url}"
        url = ShortenerTable.objects.get(short_url=short_url)
        # Increment visit count
        url.increment_visit_count()

        # Redirect to the original URL
        return redirect(url.original_url)
    except ShortenerTable.DoesNotExist:
        return JsonResponse({'error': 'Short URL does not exist'}, status=404)


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            print("User created successfully")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            print("User logged in successfully")
            messages.success(request, "Registration successful.")
            return redirect("homepage")
    else:
        form = UserCreationForm()
    context = {'form': form}

    return render(request, 'register.html', context=context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect("login")
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect("homepage")


def dashboard(request):
    # Filter links by the currently logged-in user's username
    if request.user.is_authenticated:
        username = request.user.username
        shorts = ShortenerTable.objects.filter(created_by=username)
        return render(request, 'dashboard.html', {"links": shorts})
    else:
        return render(request, 'dashboard.html', {"links": None})


def delete_url(request, delete_url):
    print(delete_url)
    if request.method == 'POST':
        form = DeleteLinkForm(request.POST)
        if form.is_valid():
            link_id = form.cleaned_data['link_id']
            link = ShortenerTable.objects.get(id=link_id)
            link.delete()
    return redirect('dashboard')
