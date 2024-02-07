from django.shortcuts import render, redirect
from .models import (Products,
                     Category)
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm


def home_page(request):
    products = Products.objects.all()
    return render(request, "index.html", {'products': products})


def about(request):
    return render(request, "about.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'با موافقیت وارد شدید ')
            return redirect('home')
        else:
            messages.error(request, "مجدد وارد شوید ")
            return redirect("login_user")
    else:
        return render(request, "login.html")


def register_user(request):
    if request.user.is_authenticated:
        return redirect("home")

    register_form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if register_form.is_valid():
            user_name = register_form.cleaned_data.get('first_name')
            password = register_form.cleaned_data.get('password1')
            email = register_form.cleaned_data.get('email')
            User.objects.create_user(username=user_name, password=password, email=email)
            return redirect("login_user")

    context = {'register_form': register_form}
    return render(request, "register.html", context)


def logout_user(request):
    logout(request)
    messages.success(request, "خروج شما با موفقیت انجام شد ")
    return render(request, "logout.html")


def product(request, pk):
    products = Products.objects.get(id=pk)
    return render(request, "product.html ", {'products': products})


def category(request, cat):
    cat = cat.replace("-", " ")  # Remove hyphens from the category name
    try:
        category = Category.objects.get(name=cat)
        products = Products.objects.filter(category=category)
        return render(request, "category.html", {'products': products, 'category': category})
    except Category.DoesNotExist:
        print(54545454)
        return redirect("home")
