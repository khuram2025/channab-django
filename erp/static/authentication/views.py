from curses.ascii import isalnum
from email import message
from urllib import request
from django.shortcuts import render, redirect
from django.views import View

import json 
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.



class UsernameValidationView(View):
    def post(self, request):
        data= json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should only contain alphanumeric character'}, status = 400)
        if User.objects.filter(username= username).exists():
            return JsonResponse({'username_error': 'Sorry Username already taken'}, status = 409)

        return JsonResponse({'username_valid': True})

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')


    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']


        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email = email).exists():

                if len(password)<6:
                    message.error(request, "Password too short")
                    return render(request, 'authentication/register.html', context)

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                
                user.save()

                message.error(request, "Account created ")
                return render(request, 'authentication/register.html')



        return render(request, 'authentication/register.html')



class LoginView(View):

    def get(self, request):
        return render(request, 'authentication/login.html')

    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']


        if username and password:
            user = auth.authenticate(username = username, password = password)
            if user:
                if user.is_active:
                    auth.login(request, user)   
                return redirect("expenses")
            return render(request, 'authentication/login.html')
        return render(request, 'authentication/login.html')

class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        return redirect('login')