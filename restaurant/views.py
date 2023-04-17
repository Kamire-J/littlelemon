from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import generics

from .models import Booking, Menu 
from .serializers import bookingSerializer, menuSerializer

# App views
def index(request):
    return render(request, 'index.html', {})



class bookingView(generics.ListCreateAPIView):

    def get(self, request):
        items = Booking.objects.all 
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data)  # Returns a json format data
    

class menuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all 
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

    
