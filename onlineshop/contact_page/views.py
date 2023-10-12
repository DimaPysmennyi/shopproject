from django.shortcuts import render

# Create your views here.
def show_contacts(request):
    return render(request, "contact_page/contacts.html")