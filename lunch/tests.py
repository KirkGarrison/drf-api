from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Lunch

# Create your tests here.


class LunchTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()
        test_lunch = Lunch.objects.create(
            name = 'Chicken teriyaki',
            customer = testuser1,
            description = 'Juicy chicken drizzled with teriyaki sauce',
        )
        test_lunch.save()


    def test_lunch_content(self):
        lunch = Lunch.objects.get(id=1)
        actual_name = str(lunch.name)
        actual_customer = str(lunch.customer)
        actual_description = str(lunch.description)
        self.assertEqual(actual_name, 'Chicken teriyaki')
        self.assertEqual(actual_customer, 'testuser1')
        self.assertEqual(actual_description, 'Juicy chicken drizzled with teriyaki sauce')
        
