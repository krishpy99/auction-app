from django.shortcuts import render
from .models import Users
def testmysql(request):
    user = Users.objects.all()
    context = {
    'userid': user[1].userid,
    'name': user[1].name,
    }
    return render(request, 'home.html', context)