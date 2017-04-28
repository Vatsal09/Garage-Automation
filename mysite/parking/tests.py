from django.test import TestCase
from parking.models import Parking_Lot, Spot, Session, ActiveSession, Image
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime
import time

# Create your tests here.

class Parking_LotModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Parking_Lot.objects.create(address = "123 SomeAddress SomeCity, SomeState SomeZip", max_levels = "5", max_spots = "300")
		Parking_Lot.objects.create(address = "567 Address City, State Zip", max_levels = "3", max_spots = "100")

	def test_address_label(self):
		parkingLot1 = Parking_Lot.objects.get(id=1)
		parkingLot2 = Parking_Lot.objects.get(id=2)
		field_label_1 = parkingLot1._meta.get_field('address').verbose_name
		field_label_2 = parkingLot2._meta.get_field('address').verbose_name
		self.assertEquals(field_label_1, 'address')
		self.assertEquals(field_label_2, 'address')

	def test_address_max_length(self):
		parkingLot1 = Parking_Lot.objects.get(id=1)
		parkingLot2 = Parking_Lot.objects.get(id=2)
		max_length_1 = parkingLot1._meta.get_field('address').max_length
		max_length_2 = parkingLot2._meta.get_field('address').max_length
		self.assertEquals(max_length_1, 150)
		self.assertTrue(max_length_2, 1000)

	def test_max_levels_label (self):
		parkingLot1 = Parking_Lot.objects.get(id=1)
		parkingLot2 = Parking_Lot.objects.get(id=2)
		field_label_1 = parkingLot1._meta.get_field('max_levels').verbose_name
		field_label_2 = parkingLot2._meta.get_field('max_levels').verbose_name
		self.assertEquals(field_label_1, "max levels")
		self.assertEquals(field_label_2, "max levels")

	def test_max_length_max_length(self):
		parkingLot1 = Parking_Lot.objects.get(id=1)
		parkingLot2 = Parking_Lot.objects.get(id=2)
		max_length_1 = parkingLot1._meta.get_field('max_levels').max_length
		max_length_2 = parkingLot2._meta.get_field('max_levels').max_length
		self.assertEquals(max_length_1, 3)
		self.assertTrue(max_length_2, 0)

	def test_max_spots_label (self):
		parkingLot1 = Parking_Lot.objects.get(id=1)
		parkingLot2 = Parking_Lot.objects.get(id=2)
		field_label_1 = parkingLot1._meta.get_field('max_spots').verbose_name
		field_label_2 = parkingLot2._meta.get_field('max_spots').verbose_name
		self.assertEquals(field_label_1, "max spots")
		self.assertEquals(field_label_2, "max spots")

	def test_max_spots_max_length(self):
		parkingLot1 = Parking_Lot.objects.get(id=1)
		parkingLot2 = Parking_Lot.objects.get(id=2)
		max_length_1 = parkingLot1._meta.get_field('max_spots').max_length
		max_length_2 = parkingLot2._meta.get_field('max_spots').max_length
		self.assertEquals(max_length_1, 5)
		self.assertTrue(max_length_2, 0)

	def test_strOfself(self):
		parkingLot1 = Parking_Lot.objects.get(id=1)
		parkingLot2 = Parking_Lot.objects.get(id=2)
		expected_object_id_1 = '%s' % (parkingLot1.id)
		expected_object_id_2 = '%s' % (parkingLot2.id)
		self.assertEquals(expected_object_id_1, str(parkingLot1))
		self.assertEquals(expected_object_id_2, str(parkingLot2))


class SpotModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		parkingLot = Parking_Lot.objects.create(address = "123 SomeAddress SomeCity, SomeState SomeZip", max_levels = "5", max_spots = "300")
		Spot.objects.create(parkingLot = parkingLot, spot_number = "1", sensor_id = "0000000001", level = "1")
		Spot.objects.create(parkingLot = parkingLot, spot_number = "332", sensor_id = "0010101001", level = "4")

	def test_spot_number_label(self):
		spot1 = Spot.objects.get(id=1)
		spot2 = Spot.objects.get(id=2)
		field_label_1 = spot1._meta.get_field('spot_number').verbose_name
		field_label_2 = spot2._meta.get_field('spot_number').verbose_name
		self.assertEquals(field_label_1, 'spot number')
		self.assertEquals(spot1.spot_number, 1)
		self.assertEquals(field_label_2, 'spot number')
		self.assertEquals(spot2.spot_number, 332)

	def test_sensor_id_label(self):
		spot1 = Spot.objects.get(id=1)
		spot2 = Spot.objects.get(id=2)
		field_label_1 = spot1._meta.get_field('sensor_id').verbose_name
		field_label_2 = spot2._meta.get_field('sensor_id').verbose_name
		self.assertEquals(field_label_1, 'sensor id')
		self.assertEquals(spot1.sensor_id, "0000000001")
		self.assertEquals(field_label_2, 'sensor id')
		self.assertEquals(spot2.sensor_id, "0010101001")


	def test_sensor_id_max_length(self):
		spot1 = Spot.objects.get(id=1)
		spot2 = Spot.objects.get(id=2)
		max_length_1 = spot1._meta.get_field('sensor_id').max_length
		max_length_2 = spot2._meta.get_field('sensor_id').max_length
		self.assertEquals(max_length_1, 10)
		self.assertTrue(max_length_2, 5)

	def test_level_label(self):
		spot1 = Spot.objects.get(id=1)
		spot2 = Spot.objects.get(id=2)
		field_label_1 = spot1._meta.get_field('level').verbose_name
		field_label_2 = spot2._meta.get_field('level').verbose_name
		self.assertEquals(field_label_1, 'level')
		self.assertEquals(spot1.level, "1")
		self.assertEquals(field_label_2, 'level')
		self.assertEquals(spot2.level, "4")


	def test_level_max_length(self):
		spot1 = Spot.objects.get(id=1)
		spot2 = Spot.objects.get(id=2)
		max_length_1 = spot1._meta.get_field('level').max_length
		max_length_2 = spot2._meta.get_field('level').max_length
		self.assertEquals(max_length_1, 3)
		self.assertTrue(max_length_2, 5)

	def test_is_occupied_label(self):
		spot1 = Spot.objects.get(id=1)
		spot2 = Spot.objects.get(id=2)
		field_label_1 = spot1._meta.get_field('is_occupied').verbose_name
		self.assertEquals(field_label_1, 'is occupied')
		self.assertFalse(spot1.is_occupied)
		spot2.is_occupied = True
		self.assertTrue(spot2.is_occupied)

	def test_is_disabled_label(self):
		spot1 = Spot.objects.get(id=1)
		spot2 = Spot.objects.get(id=2)
		field_label_1 = spot1._meta.get_field('is_disabled').verbose_name
		self.assertEquals(field_label_1, 'is disabled')
		self.assertFalse(spot1.is_disabled)
		spot2.is_disabled = True
		self.assertTrue(spot2.is_disabled)

	def test_strOfself(self):
		spot1 = Spot.objects.get(id=1)
		spot2 = Spot.objects.get(id=2)
		expected_object_id_1 = '%s - %s : %s' % (spot1.spot_number, spot1.sensor_id, "Not Occupied")
		expected_object_id_2 = '%s - %s : %s' % (spot2.spot_number, spot2.sensor_id, "Not Occupied")
		self.assertEquals(expected_object_id_1, str(spot1))
		self.assertEquals(expected_object_id_2, str(spot2))

class SessionModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		parkingLot = Parking_Lot.objects.create(address = "123 SomeAddress SomeCity, SomeState SomeZip", max_levels = "5", max_spots = "300")
		Session.objects.create(parkingLot = parkingLot, Credit_Card = "1234567812345678", license_plate_number = "ABC1234", time_arrived = "12:00:45", time_exited = "14:00:45", stay_length = "2", date_arrived = "04/15/2017", date_exited = "04/15/2017", amount_charged = "10", user_type = "1")
	def test_Credit_Card_label(self):
		session1 = Session.objects.get(id=1)
		field_label_1 = session1._meta.get_field('Credit_Card').verbose_name
		self.assertEquals(field_label_1, 'Credit Card')
		self.assertEquals(len(session1.Credit_Card), 16)
	def test_Credit_Card_max_length(self):
		session1 = Session.objects.get(id=1)
		max_length_1 = session1._meta.get_field('Credit_Card').max_length
		self.assertEquals(max_length_1, 16)
	def test_license_plate_number_label(self):
		session1 = Session.objects.get(id=1)
		field_label_1 = session1._meta.get_field('license_plate_number').verbose_name
		self.assertEquals(field_label_1, 'license plate number')
		self.assertEquals(len(session1.license_plate_number), 7)
	def test_license_plate_number_max_length(self):
		session1 = Session.objects.get(id=1)
		max_length_1 = session1._meta.get_field('license_plate_number').max_length
		self.assertEquals(max_length_1, 7)
	def test_date_arrived_label(self):
		session1 = Session.objects.get(id=1)
		field_label_1 = session1._meta.get_field('date_arrived').verbose_name
		self.assertEquals(field_label_1, 'date arrived')
	def test_date_arrived_max_length(self):
		session1 = Session.objects.get(id=1)
		max_length_1 = session1._meta.get_field('date_arrived').max_length
		self.assertEquals(max_length_1, 10)
	def test_date_exited_label(self):
		session1 = Session.objects.get(id=1)
		field_label_1 = session1._meta.get_field('date_exited').verbose_name
		self.assertEquals(field_label_1, 'date exited')
	def test_date_exited_max_length(self):
		session1 = Session.objects.get(id=1)
		max_length_1 = session1._meta.get_field('date_exited').max_length
		self.assertEquals(max_length_1, 10)
	def test_time_arrived_label(self):
		session1 = Session.objects.get(id=1)
		field_label_1 = session1._meta.get_field('time_arrived').verbose_name
		self.assertEquals(field_label_1, 'time arrived')
	def test_time_arrived_max_length(self):
		session1 = Session.objects.get(id=1)
		max_length_1 = session1._meta.get_field('time_arrived').max_length
		self.assertEquals(max_length_1, 10)
	def test_time_exited_label(self):
		session1 = Session.objects.get(id=1)
		field_label_1 = session1._meta.get_field('time_exited').verbose_name
		self.assertEquals(field_label_1, 'time exited')
	def test_time_exited_max_length(self):
		session1 = Session.objects.get(id=1)
		max_length_1 = session1._meta.get_field('time_exited').max_length
		self.assertEquals(max_length_1, 10)
	def test_staylength(self):
		session1 = Session.objects.get(id=1)
		self.assertTrue(session1.date_exited >= session1.date_arrived)
		self.assertTrue(session1.time_exited >= session1.time_arrived)
		stay_length1 = int(session1.time_exited[:2]) - int(session1.time_arrived[:2])
		self.assertEquals(str(stay_length1), session1.stay_length)		
	def test_user_type(self):
		session1 = Session.objects.get(id=1)		
		user_type = session1.user_type
		self.assertTrue(user_type == "1" or user_type == "2" or user_type == "3") 
	def test_amount_charged_label(self):
		session1 = Session.objects.get(id=1)
		stay_length = int(session1.time_exited[:2]) - int(session1.time_arrived[:2])
		amount_charged1 = str(stay_length* 5)
		self.assertEquals(amount_charged1, session1.amount_charged)
		field_label_1 = session1._meta.get_field('amount_charged').verbose_name
		self.assertEquals(field_label_1, 'amount charged')
	def test_amount_charged_max_length(self):
		session1 = Session.objects.get(id=1)
		max_length_1 = session1._meta.get_field('amount_charged').max_length
		self.assertEquals(max_length_1, 5)
	def test_strOfself(self):
		session1 = Session.objects.get(id=1)
		expected_object_id_1 = '%s' % (session1.id)		
		self.assertEquals(expected_object_id_1, str(session1))

class ActiveSessionModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		parkingLot = Parking_Lot.objects.create(address = "123 SomeAddress SomeCity, SomeState SomeZip", max_levels = "5", max_spots = "300")
		Session.objects.create(parkingLot = parkingLot, Credit_Card = "1234567812345678", license_plate_number = "ABC1234", time_arrived = "12:00:45", time_exited = "14:00:45", stay_length = "2", date_arrived = "04/15/2017", date_exited = "04/15/2017", amount_charged = "10", user_type = "1")
	def test_Credit_Card_label(self):
		session1 = Session.objects.get(id=1)
		field_label_1 = session1._meta.get_field('Credit_Card').verbose_name
		self.assertEquals(field_label_1, 'Credit Card')
		self.assertEquals(len(session1.Credit_Card), 16)
	def test_Credit_Card_max_length(self):
		session1 = Session.objects.get(id=1)
		max_length_1 = session1._meta.get_field('Credit_Card').max_length
		self.assertEquals(max_length_1, 16)
	def test_license_plate_number_label(self):
		session1 = Session.objects.get(id=1)
		field_label_1 = session1._meta.get_field('license_plate_number').verbose_name
		self.assertEquals(field_label_1, 'license plate number')
		self.assertEquals(len(session1.license_plate_number), 7)
	def test_license_plate_number_max_length(self):
		session1 = Session.objects.get(id=1)
		max_length_1 = session1._meta.get_field('license_plate_number').max_length
		self.assertEquals(max_length_1, 7)
	def test_date_arrived_label(self):
		session1 = Session.objects.get(id=1)
		field_label_1 = session1._meta.get_field('date_arrived').verbose_name
		self.assertEquals(field_label_1, 'date arrived')
	def test_date_arrived_max_length(self):
		session1 = Session.objects.get(id=1)
		max_length_1 = session1._meta.get_field('date_arrived').max_length
		self.assertEquals(max_length_1, 10)
	def test_date_exited_label(self):
		session1 = Session.objects.get(id=1)
		field_label_1 = session1._meta.get_field('date_exited').verbose_name
		self.assertEquals(field_label_1, 'date exited')
	def test_date_exited_max_length(self):
		session1 = Session.objects.get(id=1)
		max_length_1 = session1._meta.get_field('date_exited').max_length
		self.assertEquals(max_length_1, 10)
	def test_time_arrived_label(self):
		session1 = Session.objects.get(id=1)
		field_label_1 = session1._meta.get_field('time_arrived').verbose_name
		self.assertEquals(field_label_1, 'time arrived')
	def test_time_arrived_max_length(self):
		session1 = Session.objects.get(id=1)
		max_length_1 = session1._meta.get_field('time_arrived').max_length
		self.assertEquals(max_length_1, 10)
	def test_time_exited_label(self):
		session1 = Session.objects.get(id=1)
		field_label_1 = session1._meta.get_field('time_exited').verbose_name
		self.assertEquals(field_label_1, 'time exited')
	def test_time_exited_max_length(self):
		session1 = Session.objects.get(id=1)
		max_length_1 = session1._meta.get_field('time_exited').max_length
		self.assertEquals(max_length_1, 10)
	def test_staylength(self):
		session1 = Session.objects.get(id=1)
		self.assertTrue(session1.date_exited >= session1.date_arrived)
		self.assertTrue(session1.time_exited >= session1.time_arrived)
		time.sleep(3)
		stay_length1 = int(session1.time_exited[:2]) - int(session1.time_arrived[:2])
		self.assertEquals(str(stay_length1), session1.stay_length)		
	def test_user_type(self):
		session1 = Session.objects.get(id=1)		
		user_type = session1.user_type
		self.assertTrue(user_type == "1" or user_type == "2" or user_type == "3") 
	def test_amount_charged_label(self):
		session1 = Session.objects.get(id=1)
		stay_length = int(session1.time_exited[:2]) - int(session1.time_arrived[:2])
		amount_charged1 = str(stay_length* 5)
		self.assertEquals(amount_charged1, session1.amount_charged)
		field_label_1 = session1._meta.get_field('amount_charged').verbose_name
		self.assertEquals(field_label_1, 'amount charged')
	def test_amount_charged_max_length(self):
		session1 = Session.objects.get(id=1)
		max_length_1 = session1._meta.get_field('amount_charged').max_length
		self.assertEquals(max_length_1, 5)
	def test_strOfself(self):
		session1 = Session.objects.get(id=1)
		expected_object_id_1 = '%s' % (session1.id)		
		self.assertEquals(expected_object_id_1, str(session1))

class ImageModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		image = Image.objects.create(image = "pics/us-4", uploaded_at = "2017-04-23 02:10:05.155002")		
	def test_image(self):
		self.assertEquals(Image.objects.count(), 1)
	def test_strOfself(self):
		image1 = Image.objects.get(id=1)
		expected_object_id_1 = '%s' % (image1.id)		
		self.assertEquals(expected_object_id_1, str(image1))
		
		







