from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse



# Create your views here.


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if str(username).isalnum():
            return JsonResponse({"Username should only contain alphanumeric characters (A to Z and 0 to 9.)"})
        return JsonResponse({'username_valid', True})

class RegistrationView(View):
    def get(self, request):
        return render(request, "authentication2/register.html")