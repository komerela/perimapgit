from django.test import TestCase
from models import CustomUser 
# Create your tests here.

class CustomUserTestCase(TestCase):
	def setUp(self):
		CustomUser.objects.create(username="koome", phone_number="+11141331234")
		CustomUser.objects.create(username="kiasi", phone_number="+34445556262")

	def test_create_users(self):
		""" Users can be created in platform """
		koome = CustomUser.objects.get(username="koome")
		kiasi = CustomUser.objects.get(username="kiasi")
		self.assertEqual(koome.number(), 'Koome number "+11141331234"')
		self.assertEqual(kiasi.number(), 'Kiasi number "+34445556262"')