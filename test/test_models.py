from django.test import TestCase
from restaurant.models import Menu, Booking

# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_items(self):
        item = Menu.objects.create(title="Icecream", price=80, inventory=100)
        itemstr = item.get_item() 

        self.assertEqual(itemstr, "Icecream : 80")