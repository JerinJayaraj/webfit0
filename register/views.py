from django.shortcuts import render
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):

    if request.method=='POST':
       useranme = request.POST['username']
       user= auth.authenticate(usernme=username)
       return render(request, 'a.html')
    else:
        return render(request, 'home.html')