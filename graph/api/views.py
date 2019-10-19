from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'pages/index.html')


def detail(request):
    return render(request,'pages/detail.html')


def ingredient(request):
    return render(request,'pages/ingrediant.html')