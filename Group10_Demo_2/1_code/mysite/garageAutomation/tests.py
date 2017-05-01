from django.test import TestCase
from garageAutomation.models import PaymentMethod, Account, Vehicle, ParkingSession
from django.contrib.auth.models import User
import datetime
import time
class PaymentMethodModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		PaymentMethod.objects.create(type = "credit", card_number = "1234567812345678", exp = "01/20", cvv = "495", country = "United States", zip = "08854")
		PaymentMethod.objects.create(type = "debit", card_number = "2468135724681357", exp = "05/22", cvv = "579", country = "United States", zip = "07306")

	def test_type_label(self):
		payment_method_1 = PaymentMethod.objects.get(id=1)
		payment_method_2 = PaymentMethod.objects.get(id=2)
		field_label_1 = payment_method_1._meta.get_field('type').verbose_name
		self.assertEquals(field_label_1, "type")
		self.assertTrue(payment_method_1.type.lower() == "credit" or payment_method_1.type.lower() == "debit")

	def test_type_max_length(self):
		payment_method_1 = PaymentMethod.objects.get(id=1)
		payment_method_2 = PaymentMethod.objects.get(id=2)
		max_length_1 = payment_method_1._meta.get_field('type').max_length
		max_length_2 = payment_method_2._meta.get_field('type').max_length
		self.assertEquals(max_length_1, 6)
		self.assertTrue(max_length_2, 10)

	def test_card_number_label(self):
		payment_method_1 = PaymentMethod.objects.get(id=1)
		payment_method_2 = PaymentMethod.objects.get(id=2)
		self.assertEquals(len(payment_method_1.card_number), 16)
		self.assertEquals(len(payment_method_2.card_number), 16)
		self.assertTrue(payment_method_1.card_number.isdigit())
		self.assertTrue(payment_method_2.card_number.isdigit())

	def test_card_number_max_length(self):
		payment_method_1 = PaymentMethod.objects.get(id=1)
		payment_method_2 = PaymentMethod.objects.get(id=2)
		max_length_1 = payment_method_1._meta.get_field('card_number').max_length
		max_length_2 = payment_method_2._meta.get_field('card_number').max_length
		self.assertEquals(max_length_1, 16)
		self.assertTrue(max_length_2, 10)

	def test_exp_label(self):
		payment_method_1 = PaymentMethod.objects.get(id=1)
		payment_method_2 = PaymentMethod.objects.get(id=2)
		field_label_1 = payment_method_1._meta.get_field('exp').verbose_name
		field_label_2 = payment_method_2._meta.get_field('exp').verbose_name
		self.assertEquals(field_label_1, "exp")
		self.assertEquals(field_label_2, "exp")		

	def test_exp_max_length(self):
		payment_method_1 = PaymentMethod.objects.get(id=1)
		payment_method_2 = PaymentMethod.objects.get(id=2)
		max_length_1 = payment_method_1._meta.get_field('exp').max_length
		max_length_2 = payment_method_2._meta.get_field('exp').max_length
		self.assertEquals(max_length_1, 5)
		self.assertTrue(max_length_2, 7)

	def test_cvv_label(self):
		payment_method_1 = PaymentMethod.objects.get(id=1)
		payment_method_2 = PaymentMethod.objects.get(id=2)
		self.assertEquals(len(payment_method_1.cvv), 3)
		self.assertEquals(len(payment_method_2.cvv), 3)
		self.assertTrue(payment_method_1.card_number.isdigit())
		self.assertTrue(payment_method_2.card_number.isdigit())

	def test_cvv_max_length(self):
		payment_method_1 = PaymentMethod.objects.get(id=1)
		payment_method_2 = PaymentMethod.objects.get(id=2)
		max_length_1 = payment_method_1._meta.get_field('cvv').max_length
		max_length_2 = payment_method_2._meta.get_field('cvv').max_length
		self.assertEquals(max_length_1, 3)
		self.assertTrue(max_length_2, 2)

	def test_country_label(self):
		payment_method_1 = PaymentMethod.objects.get(id=1)
		payment_method_2 = PaymentMethod.objects.get(id=2)
		field_label_1 = payment_method_1._meta.get_field('country').verbose_name
		field_label_2 = payment_method_2._meta.get_field('country').verbose_name
		self.assertEquals(field_label_1, 'country')
		self.assertEquals(field_label_2, 'country')

	def test_country_max_length(self):
		payment_method_1 = PaymentMethod.objects.get(id=1)
		payment_method_2 = PaymentMethod.objects.get(id=2)
		max_length_1 = payment_method_1._meta.get_field('country').max_length
		max_length_2 = payment_method_2._meta.get_field('country').max_length
		self.assertEquals(max_length_1, 30)
		self.assertTrue(max_length_2, 35)

	def test_zip_label(self):
		payment_method_1 = PaymentMethod.objects.get(id=1)
		payment_method_2 = PaymentMethod.objects.get(id=2)
		self.assertEquals(len(payment_method_1.zip), 5)
		self.assertEquals(len(payment_method_2.zip), 5)
		self.assertTrue(payment_method_1.card_number.isdigit())
		self.assertTrue(payment_method_2.card_number.isdigit())

	def test_zip_max_length(self):
		payment_method_1 = PaymentMethod.objects.get(id=1)
		payment_method_2 = PaymentMethod.objects.get(id=2)
		max_length_1 = payment_method_1._meta.get_field('zip').max_length
		max_length_2 = payment_method_2._meta.get_field('zip').max_length
		self.assertEquals(max_length_1, 5)
		self.assertTrue(max_length_2, 4)

	def test_getLastFour(self):
		payment_method_1 = PaymentMethod.objects.get(id=1)
		payment_method_2 = PaymentMethod.objects.get(id=2)
		self.assertEquals(len(payment_method_1.getLastFour()), 4)
		self.assertEquals(len(payment_method_2.getLastFour()), 4)

	def test_strOfself(self):
		payment_method_1 = PaymentMethod.objects.get(id=1)
		payment_method_2 = PaymentMethod.objects.get(id=2)
		expected_object_1 = '%s' % (payment_method_1.getLastFour())
		expected_object_2 = '%s' % (payment_method_2.getLastFour())
		self.assertEquals(expected_object_1, str(payment_method_1))
		self.assertEquals(expected_object_2, str(payment_method_2))

