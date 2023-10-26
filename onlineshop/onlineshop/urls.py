"""
URL configuration for onlineshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_page.views import show_main
from contact_page.views import show_contacts
from product_page.views import show_products
from shopping_cart_page.views import show_cart
from Authorization_Registration.views import show_login, show_registration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', show_main, name= "main"),
    path('contacts/', show_contacts, name= "contacts"),
    path('products/', show_products, name= "products"),
    path('shopping_cart/', show_cart, name= "shopping_cart"),
    path('login/', show_login, name="login"),
    path('', show_registration, name="registration")
]
