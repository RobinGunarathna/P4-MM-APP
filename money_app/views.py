from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'templates/mapp/index2.html')

def add_mapp(request):
    return render(request, 'templates/Mapp/add_mapp.html')