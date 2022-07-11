from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'templates/index.html')

def add_mapp(request):
    return render(request, 'templates/add_mapp.html')