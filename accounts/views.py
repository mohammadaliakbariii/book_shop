from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm
from django.shortcuts import render

# Create your views here.
def sign_up(request):
    if request.method=="POST":
        email=request.POST['email']
        full_name = request.POST['full_name']
        password=request.POST['pass1']
        password2=request.POST['pass2']
        if  CustomUser.objects.filter(email=email):
            message='this username or email is already exit please choose another please'
            return render(request,'accounts/sign_up.html',context={'message':message})
        if password!=password2:
            message = 'passwords are not match!!!'
            return render(request, 'accounts/sign_up.html', context={'message':message})

        newuser=CustomUser.objects.create_user(email=email,full_name = full_name,password=password)
        newuser.full_name = full_name
        newuser.save()
        message='signUp successfully!!!please logIN'
        return redirect('store:all_products')
    else:
        return render(request,'accounts/sign_up.html')

def login_customer(request):
    message = None
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None and user.is_staff==False:
                login(request, user)
                message = f'welcome dear {user.full_name}'
                if 'next' in request.GET:
                    return HttpResponseRedirect(request.GET['next'])
                return redirect('store:all_products')
            else:
                message = 'username or password is wrong!!!please try again'
    return render(request, 'accounts/login_customer.html', context={
        'form': form,
        'message': message
    })


def login_staff(request):
    message = None
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None and user.is_staff==True:
                login(request, user)
                message = f'welcome dear {user.full_name}'
                if 'next' in request.GET:
                    return HttpResponseRedirect(request.GET['next'])
                return redirect('store:all_products')
            else:
                message = 'username or password is wrong!!!please try again'
    return render(request, 'accounts/login_staff.html', context={
        'form': form,
        'message': message
    })



def logOut(request):
    logout(request)
    return redirect('store:all_products')
