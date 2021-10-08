from django.shortcuts import render

# Create your views here.
def sign_up(request):
    return render(request,'accounts/sign_up.html',context={

    })


def login_customer(request):
    return render(request, 'accounts/login_customer.html', context={

    })
def login_staff(request):
    return render(request,'accounts/login_staff.html',context={

    })