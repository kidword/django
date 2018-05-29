from django.shortcuts import render,redirect,reverse
from  .models import *
from  django.http import HttpResponse

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        users = ShoppingOperation.objects.filter(username=user, password=pwd)
        if len(users)==1 :
            session['username']=user
            return render(request,'home1.html')

        else:
            return render(request, 'login.html')

def home1(requset):
    return render(requset, 'home1.html')
def register(requset):
    if requset.method == 'GET':
     return render(requset, 'register.html')
    else:
        user = ShoppingOperation()
        user.username = requset.POST.get('username')
        user.password = requset.POST.get('password')
        if len(user.username)>=0:
            user.save()
            return render(requset, 'login.html')
        else:
            return render(requset,'register.html')


def options(requset):
    if requset.method=='GET':
        return render(requset,'options.html')
    else:
        pwd = requset.POST.get('password')
        users = ShoppingOperation.objects.filter(username='1').first().delete()
        print('           --------            ',users.password)

        if users.password==pwd:
            users.password = requset.POST.get('npassword')
            print('',users.password)
            users.save()
            return render(requset, 'login.html')
        else:
            return render(requset, 'options.html')
        return render(requset,'options.html')
def pay(requset):
    if requset.method == 'GET':
        return render(requset, 'pay.html')
    else:
     if requset.POST.get('add'):
        p = pay()
        p.sum=requset.POST.get('box')*39+10
        print(p.sum)



    return render(requset, 'pay.html')