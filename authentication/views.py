from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
import json
from django.http import JsonResponse



# Create your views here.


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({"Username should only contain alphanumeric characters (A to Z and 0 to 9"}, status = 400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({"Username is allready in use"}, status = 409)
        
        return JsonResponse({'username_valid' : True})

class RegistrationView(View):
    def get(self, request):
        return render(request, "authentication2/register.html")