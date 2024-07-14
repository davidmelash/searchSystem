import json

from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from .forms import SignupForm, LoginForm
from .search_engine import make_search


# Create your views here.
# Home page
def index(request):
    if request.user.is_authenticated:
        print('authenticated')
        return render(request, 'search/index.html')
    else:
        print('not authenticated')
        return render(request, 'auth/login.html')


# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                print('invalid username or password')
                return render(request, 'auth/login.html', {'form': form})
        else:
            print(form.errors)
            print('form is invalid')
    else:
        return render(request, 'auth/login.html', )

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')


# @ensure_csrf_cookie
@csrf_exempt
def search(request):
    json_data = json.loads(request.body)
    filter_type = json_data.get("filterType").replace("\n", "").strip()
    entity_type = json_data.get("entityType").replace("\n", "").strip()
    search_value = json_data.get("searchValue").replace("\n", "").strip()
    print(f"{filter_type}|{entity_type}|{search_value}|1")
    result = make_search(filter_type, entity_type, search_value)
    response = JsonResponse(list(result), safe=False)
    return response