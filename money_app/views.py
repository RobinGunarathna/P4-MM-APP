from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Mapp/index2.html')

def add_mapp(request):
    return render(request, 'Mapp/add_mapp.html')