from django.contrib.auth.models import Group, User
from django.db import transaction
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Booking, Cart, Category, MenuItem, Order, OrderItem
from .serializers import (
    BookingSerializer,
    CategorySerializer,
    MenuItemSerializer,
    CartSerializer,
    OrderSerializer,
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


class CartView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.get_queryset().delete()
        return Response(status=status.HTTP_200_OK)


class OrderView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Manager').exists():
            return Order.objects.all()
        if user.groups.filter(name='Delivery crew').exists():
            return Order.objects.filter(delivery_crew=user)
        return Order.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        cart_items = list(Cart.objects.filter(user=request.user))
        if not cart_items:
            return Response(
                {'detail': 'Your cart is empty.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        with transaction.atomic():
            total = sum((item.price for item in cart_items), start=0)
            order = Order.objects.create(user=request.user, total=total)
            OrderItem.objects.bulk_create(
                [
                    OrderItem(
                        order=order,
                        menuitem=item.menuitem,
                        quantity=item.quantity,
                        unit_price=item.unit_price,
                        price=item.price,
                    )
                    for item in cart_items
                ]
            )
            Cart.objects.filter(user=request.user).delete()

        return Response(
            {'message': 'Order placed successfully.', 'order_id': order.id},
            status=status.HTTP_201_CREATED,
        )


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
