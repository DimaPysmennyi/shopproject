from django.shortcuts import render

# Create your views here.
def show_cart(request):
    return render(request,'shopping_cart_page/cart.html')