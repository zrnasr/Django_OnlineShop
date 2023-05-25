from django.contrib.auth import views
from django.urls import path
from user.views import login, SignUp, home, new_user

urlpatterns = [
    path('login/', login , name='login'),
    path('signup/', SignUp.as_view() , name='signup'),
    path('home/', home , name='home'),
    path('new_user/', new_user , name='new_user'),
]