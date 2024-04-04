from django.shortcuts import render
from .models import Users
def hero_page(request):
    # Add logic to fetch data for hero page
    return render(request, 'hero_page.html')



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



@login_required
def landing_page(request):
    return render(request, 'landing_page.html')
