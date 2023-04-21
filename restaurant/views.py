from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import generics, viewsets

from .models import Booking, Menu 
from .serializers import bookingSerializer, menuSerializer

# App views
def index(request):
    return render(request, 'index.html', {})

class menuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all 
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer


class bookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer

    
