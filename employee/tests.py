
from django.test import TestCase
from employee.models import Employee

class AnimalTestCase(TestCase):

	def setUp(self):
		Employee.objects.create(ename="naveen")
		Employee.objects.create(eid=123)
		Employee.objects.create(eemail="naveentej458@gmail.com")
		Employee.objects.create(econtact=1234567890)
			

	def test_check_for_name(self):
		ename = Employee.objects.get(ename="naveen")
		self.assertEqual(ename.ename, 'naveen')
		self.assertNotEqual(ename.ename, 'tej123')
		
	def test_check_for_eid(self):
		eid = Employee.objects.get(eid='123')
		self.assertNotEqual(eid.eid, 123)
		self.assertEqual(eid.eid, '123')
		
	def test_check_for_eemail(self):
		eemail = Employee.objects.get(eemail="naveentej458@gmail.com")
		self.assertEqual(eemail.eemail, 'naveentej458@gmail.com')
		self.assertNotEqual(eemail.eemail, 'naveentej')
		
	def test_check_for_econtact(self):
		econtact = Employee.objects.get(econtact="1234567890")
		self.assertEqual(econtact.econtact, '1234567890')
		self.assertNotEqual(econtact.econtact, '1234563789')
	