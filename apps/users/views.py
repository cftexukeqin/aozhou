from django.shortcuts import render,redirect,reverse
from django.contrib.auth import login,logout,authenticate
from .forms import LoginForm,SignupForm
from .models import UserProfile
from utils import restful

# Create your views here.

def my_login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('pwd')
            next = form.cleaned_data.get("next")
            if next:
                next_url = next.split("=")[1]
            else:
                next_url = ""
            user = authenticate(request,username=telephone,password=password)
            # print("user",user)
            if user:
                login(request,user)
                request.session.set_expiry(None)
                data = {
                    "next_url":next_url
                }
                return restful.result(data=data)
            else:
                return restful.noauth(message="没有这个用户")
        else:
            print(form.get_error())
            return restful.paramserror(form.get_error())

def regist(request):
    if request.method == "GET":
        return render(request,'regist.html')
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            pwd1 = form.cleaned_data.get('pwd1')
            print("telephone:",telephone)
            print(pwd1)
            # pwd2 = form.cleaned_data.get('pwd2')
            user = UserProfile.objects.create_user(username=telephone,mobile=telephone, password=pwd1)
            login(request, user)
            return restful.ok()
        else:
            return restful.paramserror(form.get_error())


def my_logout(request):
    logout(request)
    return redirect(reverse('goods:index'))