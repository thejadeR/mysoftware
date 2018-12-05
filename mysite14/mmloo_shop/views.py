from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from mmloo_shop.models import UserInfo


def index(request):
    return render(request,'index.html')


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        uname = request.POST.get('uname')
        upassword = request.POST.get('upassword')
        user = UserInfo.objects.filter(db_uname=uname).filter(db_password=upassword)
        if user.count():
            response = redirect('mmloo_shop:index')
            response.set_cookie('uname',uname)
            return response

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')

    elif request.method == 'POST':
        u = UserInfo()

        u.db_uname = request.POST.get('uname')
        u.db_upassword = request.POST.get('upassword')
        u.save()

        response = redirect('mmloo_shop:index')
        response.set_cookie('uname',u.db_uname)
        return response


def cart(request):
    if request.method == 'GET':
        return render(request,'tb-cart.html')