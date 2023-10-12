from django.shortcuts import render

# Create your views here.
def show_products(request):
    return render(request, "product_page/products.html")