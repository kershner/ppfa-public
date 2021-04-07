from django.core.serializers.json import DjangoJSONEncoder
from .serializers import AppointmentSerializer
from django.test import TestCase, Client
from pp.doctors.models import Doctor
from rest_framework import status
from django.utils import timezone
from datetime import datetime
from django.urls import reverse
from .models import Appointment
import json


class AppointmentTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url_prefix = 'http://localhost:8000'
        self.dummy_phone_number = '(555)555-5555'
        self.datetime = datetime(2021, 8, 15, 8, 0, tzinfo=timezone.utc)
        self.date_string = '2021-08-15T08:15'

        # Create some test doctors
        self.test_doctor = Doctor.objects.create(name='Tyler Kershner', specialization='im', rating=1)
        self.test_doctor_2 = Doctor.objects.create(name='Eugene the Dog', specialization='ne', rating=3)
        self.test_doctor_3 = Doctor.objects.create(name='Sean Jackson', specialization='de', rating=4)

        # Create an initial test appointment
        self.test_appointment = Appointment.objects.create(datetime=self.datetime,
                                                           contact_phone_number=self.dummy_phone_number,
                                                           new_patient=False)
        self.test_appointment.doctors.add(self.test_doctor)

        self.get_post_endpoint = reverse('appointments:get_post_appointments')
        self.update_delete_endpoint = reverse('appointments:get_delete_update_appointments', args=(self.test_appointment.pk,))
        self.invalid_update_delete_endpoint = reverse('appointments:get_delete_update_appointments', args=(99999,))

        self.valid_payload = {'datetime': self.date_string,
                              'contact_phone_number': self.dummy_phone_number,
                              'new_patient': False,
                              'reason': 'VC'}
        self.invalid_payload = {'datetime': '', 'contact_phone_number': ''}

    def tearDown(self):
        pass

    def test_get_appointments(self):
        response = self.client.get(self.get_post_endpoint)
        return self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_appointment(self):
        payload = self.valid_payload
        payload['doctors'] = [self.test_doctor_2.pk]
        response = self.client.post(
            self.get_post_endpoint,
            data=json.dumps(payload, cls=DjangoJSONEncoder),
            content_type='application/json'
        )
        return self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_appointment_by_pk(self):
        response = self.client.get(self.update_delete_endpoint)
        return self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_appointment(self):
        response = self.client.delete(self.update_delete_endpoint)
        return self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Additional edge cases
    def test_update_appointment_by_pk(self):
        response = self.client.put(
            self.update_delete_endpoint,
            data=AppointmentSerializer(self.test_appointment).data,
            content_type='application/json'
        )
        return self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_appointment_by_pk(self):
        response = self.client.get(self.invalid_update_delete_endpoint)
        return self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_invalid_appointment(self):
        response = self.client.post(
            self.get_post_endpoint,
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        return self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_appointment_with_doctor(self):
        payload = self.valid_payload
        payload['doctors'] = [self.test_doctor_3.pk]
        response = self.client.post(
            self.get_post_endpoint,
            data=json.dumps(payload, cls=DjangoJSONEncoder),
            content_type='application/json'
        )
        return self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_appointment_with_doctor_with_existing_appointment(self):
        payload = self.valid_payload
        payload['doctors'] = [self.test_doctor.pk]  # Doctor #1 from the initial test appointment
        response = self.client.post(
            self.get_post_endpoint,
            data=json.dumps(payload, cls=DjangoJSONEncoder),
            content_type='application/json'
        )
        return self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
