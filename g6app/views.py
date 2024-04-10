from django.db import connection
from .models import Users
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm

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

            if password == user.password:
                # Authentication successful, login the user
                # login(request, user)
                return redirect('auctions')
            else:
                error_message = 'Incorrect password'
        else:
            error_message = 'User does not exist'

        return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')



@login_required
def landing_page(request):
    return render(request, 'landing_page.html')




def admin_page(request):
    results = None
    error_message = None
    if request.method == 'POST':
        query = request.POST.get('query')
        try:
            # Execute the raw SQL query
            with connection.cursor() as cursor:
                cursor.execute(query)
                # Fetch all the rows from the cursor
                columns = [col[0] for col in cursor.description]
                results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        except Exception as e:
            error_message = str(e)
            print("Error executing query:", error_message)  
            return render(request, 'admin_page.html', {'error_message': error_message})
    return render(request, 'admin_page.html', {'results': results})
