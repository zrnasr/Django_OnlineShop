    
from shop.views import home, profile
from django.urls import reverse, path


urlpatterns = [
    path('home/', home , name='home'),
    path('profile/', profile, name='profile')
]