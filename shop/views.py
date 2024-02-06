from django.shortcuts import render,redirect
from .models import Products
from django.contrib.auth import authenticate, login, logout
from  django.contrib import messages

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
            messages.error(request,"مجدد وارد شوید ")
            return redirect("login_user")
    else:
        return render(request, "login.html")




def logout_user(request):
    logout(request)
    messages.success(request, "خروج شما با موفقیت انجام شد ")
    return render(request, "logout.html")


