from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from user.view_form.input_form import LoginForm, SignUpForm
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponseRedirect

class SignUp(View):
    def post(self, request):
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return HttpResponseRedirect ("/user/login/")
        #handle invalid form
        
    def get(self, request):
        signup_form = SignUpForm()
        return render (request, 'register.html', {'signupform': signup_form })
    
class Login(ModelBackend, View):
    def post(self, request):
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            phone = request.POST['phone']
            password = request.POST['password']
            user = authenticate(phone = phone, password = password)
            if user is None:
                return HttpResponse("Invalid credentials.")
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("form not valid.")

    def get(self, request):
        loginform = LoginForm()
        return render(request, 'login.html', {'loginform': loginform})


