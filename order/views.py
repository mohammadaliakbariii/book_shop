from django.shortcuts import render

# Create your views here.
def basket(request):
    return render(request,'order/basket.html')