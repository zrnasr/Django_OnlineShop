from django.contrib.auth import views
from django.urls import path
from user.views import Login, SignUp

urlpatterns = [
    path('login/', Login.as_view() , name='login'),
    path('signup/', SignUp.as_view() , name='signup'),
]