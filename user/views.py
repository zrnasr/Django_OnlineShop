from django.shortcuts import render, redirect
from user.input_form import LoginForm, SignUpForm
from django.views.generic import View

from django.http import HttpResponseRedirect

class SignUp(View):
    def post(self, request):
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            print("saveeeeeeeeeeeeeeeeeeeeeeeeed")
            signup_form.save()
            return HttpResponseRedirect ("/user/new_user/")
        
    def get(self, request):
        signup_form = SignUpForm()
        return render (request, 'register.html', {'signupform': signup_form })
    

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/user/home/")
    else:
        loginform = LoginForm()
    return render(request, 'login.html', {'loginform': loginform})


def home(request):
    return render(request, 'home.html')

def new_user(request):
    return render (request, "new_user.html")




            
            

