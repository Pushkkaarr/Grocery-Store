from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def store(request):
    return render(request,'store.html')

