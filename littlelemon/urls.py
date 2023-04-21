
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant import views



router = routers.DefaultRouter() 
router.register(r'tables', views.bookingView, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
]


