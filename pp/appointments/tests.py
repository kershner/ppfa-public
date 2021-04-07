from .serializers import AppointmentSerializer
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from django.utils import timezone
from .models import Appointment
import json


class AppointmentTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url_prefix = 'http://localhost:8000'
        self.dummy_phone_number = '(555)555-5555'
        self.test_appointment = Appointment.objects.create(datetime=timezone.now(),
                                                           contact_phone_number=self.dummy_phone_number,
                                                           new_patient=False)
        self.get_post_endpoint = '{}{}'.format(self.url_prefix,
                                               reverse('appointments:get_post_appointments'))
        self.update_delete_endpoint = '{}{}'.format(self.url_prefix,
                                                    reverse('appointments:get_delete_update_appointments',
                                                            args=(self.test_appointment.pk,)))

        self.invalid_update_delete_endpoint = '{}{}'.format(self.url_prefix,
                                                            reverse('appointments:get_delete_update_appointments',
                                                                    args=(99999,)))

        self.invalid_payload = {'datetime': '', 'contact_phone_number': ''}

    def tearDown(self):
        pass

    def test_get_appointments(self):
        response = self.client.get(self.get_post_endpoint)
        return self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_appointment(self):
        response = self.client.post(
            self.get_post_endpoint,
            data=AppointmentSerializer(self.test_appointment).data,
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

