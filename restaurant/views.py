from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Booking, Category, MenuItem
from .serializers import (
    BookingSerializer,
    CategorySerializer,
    MenuItemSerializer,
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsManager

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticatedOrReadOnly()]
        return [IsManager()]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticatedOrReadOnly()]
        return [IsManager()]


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ManagersView(APIView):
    permission_classes = [IsManager, IsAuthenticated]
    group_name = 'Manager'

    def get(self, request):
        group = get_object_or_404(Group, name=self.group_name)
        users = group.user_set.values('username', 'email')
        return Response(list(users))

    def post(self, request):
        group = get_object_or_404(Group, name=self.group_name)
        user = get_object_or_404(User, username=request.data.get('username'))
        group.user_set.add(user)
        return Response(
            {'message': f'{user.username} added to {self.group_name}'},
            status=status.HTTP_201_CREATED,
        )

    def delete(self, request):
        group = get_object_or_404(Group, name=self.group_name)
        user = get_object_or_404(User, username=request.data.get('username'))
        group.user_set.remove(user)
        return Response(status=status.HTTP_200_OK)


class DeliveryCrewView(APIView):
    permission_classes = [IsManager, IsAuthenticated]
    group_name = 'Delivery crew'

    def get(self, request):
        group = get_object_or_404(Group, name=self.group_name)
        users = group.user_set.values('username', 'email')
        return Response(list(users))

    def post(self, request):
        group = get_object_or_404(Group, name=self.group_name)
        user = get_object_or_404(User, username=request.data.get('username'))
        group.user_set.add(user)
        return Response(
            {'message': f'{user.username} added to {self.group_name}'},
            status=status.HTTP_201_CREATED,
        )

    def delete(self, request):
        group = get_object_or_404(Group, name=self.group_name)
        user = get_object_or_404(User, username=request.data.get('username'))
        group.user_set.remove(user)
        return Response(status=status.HTTP_200_OK)


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def index(request):
    return render(request, 'index.html', {})
