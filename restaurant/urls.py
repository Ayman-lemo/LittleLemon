from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.CategoryView.as_view()),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('cart/menu-items/', views.CartView.as_view()),
    path('orders/', views.OrderView.as_view()),
    path('orders/<int:pk>/', views.SingleOrderView.as_view()),
    path('groups/manager/users/', views.ManagersView.as_view()),
    path('groups/delivery-crew/users/', views.DeliveryCrewView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]