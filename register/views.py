from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method=='POST':
        name1=Register.objects.all()
        print(name1)

    else:
        return render(request, 'home.html')