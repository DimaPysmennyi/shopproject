from django.shortcuts import render, redirect
from Authorization_Registration.forms import RegisterForm, LoginForm
from APP_settings.models import UserForm

# Create your views here.
def show_login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "authorization_registration/login.html", {"form": form})

    if request.method == "POST":
        form = LoginForm(request.POST)
        print(form["username"].value())
        print(form["password1"].value())
        filtered_user = UserForm.objects.filter(login = form["username"].value(), password = form["password1"].value())
        print(filtered_user)
        if filtered_user:
            return redirect("/main")

        else:
            return render(request, "authorization_registration/login.html", {"form": form})
        
def show_registration(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "authorization_registration/register.html", {'form': form})
    
    if request.method == "POST":
        form = RegisterForm(request.POST) 
        if form.is_valid() and not UserForm.objects.filter(login = form["username"].value(), email = form["email"].value()):
            UserForm.objects.create(
                login = form["username"].value(), 
                password = form["password1"].value(),
                email = form["email"].value(), 
            )
            return redirect("/login")
        else:
            return render(request, 'authorization_registration/register.html', {'form': form})
    else:
        return render(request, 'authorization_registration/register.html', {'form': form})
    