from django.urls import path
from user.api.v1.views import LoginPage, RegisterPage

urlpatterns = [
    # path('profile/', ProfilePage.as_view()),
    path('login/', LoginPage.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
]