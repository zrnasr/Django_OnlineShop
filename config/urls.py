from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.api.v1.urls')),
    path('shop/', include('shop.urls')),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
]
