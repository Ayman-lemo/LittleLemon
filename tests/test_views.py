from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # إضافة بيانات وهمية للاختبار
        Menu.objects.create(title="IceCream", price=80.00, inventory=100)
        Menu.objects.create(title="Cake", price=50.00, inventory=50)

    def test_getall(self):
        client = APIClient()
        # طلب البيانات من الرابط الخاص بالقائمة
        response = client.get('/restaurant/menu/') 
        
        # جلب البيانات من قاعدة البيانات وتحويلها عبر السيريلايزر
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        # التأكد من أن البيانات المسترجعة من الـ API تطابق قاعدة البيانات
        self.assertEqual(response.data, serializer.data)