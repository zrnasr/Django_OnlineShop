from django.urls import path
from user.view_form.views import Login, SignUp


urlpatterns = [
    path('login/', Login.as_view() , name='login'),
    path('signup/', SignUp.as_view() , name='signup'),
]
