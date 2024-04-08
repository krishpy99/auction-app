from django.shortcuts import render
from .models import Users
def hero_page(request):
    # Add logic to fetch data for hero page
    return render(request, 'hero_page.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.type = 'Normal'  # Set default value for 'Type' field
            user.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Retrieve user based on email
        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            user = None
        
        if user is not None:
            if check_password(password,user.password):
                # Authentication successful, login the user
                login(request, user)
                return redirect('landing_page')
            else:
                error_message = 'Incorrect password'
        else:
            error_message = 'User does not exist'

        return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

from django.contrib.auth.hashers import check_password

def user_login(request):
    error_message = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = Users.objects.get(email=email)
                if check_password(password, user.password):
                    login(request, user)
                    return redirect('landing_page')
                else:
                    error_message = 'Invalid email or password'
            except Users.DoesNotExist:
                error_message = 'User does not exist'
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'error_message': error_message})



@login_required
def landing_page(request):
    return render(request, 'landing_page.html')
