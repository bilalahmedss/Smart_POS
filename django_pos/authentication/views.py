# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.shortcuts import render

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid username or password!'
        else:
            msg = 'An error occurred!'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'User created successfully. Please <a href="/accounts/login">login</a>.'
                success = True
        else:
            # Let the template handle displaying the form errors
            pass
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {
        "form": form,
        "msg": msg,
        "success": success
    })

def index(request):
    annual_earnings = 1234567.89  # Example earnings value
    avg_month = 12345.67  # Example monthly earnings value

    # Format the annual earnings and avg_month with commas (without Rs prefix, will be added in template)
    formatted_earnings = f"{annual_earnings:,.0f}"  
    formatted_avg_month = f"{avg_month:,.0f}"

    # Pass the formatted values to the template
    return render(request, 'index.html', {
        'annual_earnings': formatted_earnings,
        'avg_month': formatted_avg_month
    })