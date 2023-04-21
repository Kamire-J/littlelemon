
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter() 
router.register(r'tables', views.bookingView, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]


