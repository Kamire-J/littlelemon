from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated 


from .models import Booking, Menu 
from .serializers import bookingSerializer, menuSerializer

# App views
def index(request):
    return render(request, 'index.html', {})

@api_view()
@permission_classes([IsAuthenticated])
def test_message(request):
    return Response({"message":"This view is protected."})

class menuView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all 
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer


class bookingView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer

    
