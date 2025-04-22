# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import LoginForm, SignUpForm
from .models import OTP

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

def otp_password_reset_request(request):
    """
    View for requesting a password reset via OTP
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            # Generate OTP
            otp = OTP.generate_otp(user)
            
            # Send OTP via email
            subject = 'Password Reset OTP for Smart POS'
            message = f'Your OTP for password reset is: {otp.otp_code}\n\nThis OTP will expire in 15 minutes.'
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
            
            # Store user_id in session for the next step
            request.session['reset_user_id'] = user.id
            
            messages.success(request, 'OTP has been sent to your email address.')
            return redirect('authentication:otp_password_reset_verify')
        except User.DoesNotExist:
            messages.error(request, 'No user with that email address exists.')
    
    return render(request, 'accounts/otp_password_reset_request.html')

def otp_password_reset_verify(request):
    """
    View for verifying OTP and showing password reset form
    """
    user_id = request.session.get('reset_user_id')
    if not user_id:
        messages.error(request, 'Invalid request. Please try again.')
        return redirect('authentication:otp_password_reset_request')
    
    if request.method == 'POST':
        otp_code = request.POST.get('otp_code')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        try:
            user = User.objects.get(id=user_id)
            otp = OTP.objects.get(user=user, otp_code=otp_code)
            
            if not otp.is_valid():
                messages.error(request, 'OTP has expired. Please request a new one.')
                return redirect('authentication:otp_password_reset_request')
            
            if new_password != confirm_password:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'accounts/otp_password_reset_verify.html')
            
            # Set new password
            user.set_password(new_password)
            user.save()
            
            # Delete the OTP
            otp.delete()
            
            # Clear the session
            if 'reset_user_id' in request.session:
                del request.session['reset_user_id']
            
            messages.success(request, 'Password has been reset successfully. You can now log in with your new password.')
            return redirect('authentication:login')
            
        except (User.DoesNotExist, OTP.DoesNotExist):
            messages.error(request, 'Invalid OTP. Please try again.')
    
    return render(request, 'accounts/otp_password_reset_verify.html')