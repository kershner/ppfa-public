from django.test import TestCase
import requests
from .models import Appointment

class AppointmentTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_appointments(self):
        response = requests.get('http://localhost:8000/api/v1/appointments')
        pass

    def test_create_appointment(self):
        pass

    def test_delete_appointment(self):
        pass

    def test_get_appointment_by_pk(self):
        pass