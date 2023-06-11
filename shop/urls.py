    
from shop.views import home
from django.urls import reverse, path


urlpatterns = [
    path('home/', home , name='home'),
]