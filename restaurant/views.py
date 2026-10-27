from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Booking, Category, MenuItem
from .serializers import (
    BookingSerializer,
    CategorySerializer,
    MenuItemSerializer,
)
from rest_framework.permissions import IsAuthenticated


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def index(request):
    return render(request, 'index.html', {})
