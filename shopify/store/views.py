from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'store/index.html')


def cart(request):
    return render(request, 'store/cart.html')


def dashboard(request):
    return render(request, 'store/dashboard.html')


def register(request):
    return render(request, 'store/register.html')


def search(request):
    return render(request, 'store/search-result.html')


def signin(request):
    return render(request, 'store/signin.html')


def order(request):
    return render(request, 'store/order_complete.html')


def product(request):
    return render(request, 'store/product-detail.html')


def store(request):
    return render(request, 'store/store.html')
