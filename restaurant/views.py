from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 

from .models import Booking, Menu 
from .serializers import bookingSerializer, menuSerializer

# App views
def index(request):
    return render(request, 'index.html', {})



class bookingView(APIView):

    def get(self, request):
        items = Booking.objects.all 
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data)  # Returns a json format data
    

class menuView(APIView):

    def get(self, request):
        items = Menu.objects.all 
        serializer= menuSerializer(items, many=True)
        return Response(serializer.data)
    
