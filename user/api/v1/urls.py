from django.urls import path
from user.api.v1.views import LoginPage, RegisterPage, DoLogin, ProfilePage

urlpatterns = [
    path('profile/', ProfilePage.as_view(), name='profile'),
    path('login/', LoginPage.as_view(), name='login'),
    path('dologin/', DoLogin.as_view(), name='dologin'),
    path('register/', RegisterPage.as_view(), name='register'),
]