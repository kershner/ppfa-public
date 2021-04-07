from pp.doctors.serializers import DoctorSerializer
from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'datetime', 'reason', 'new_patient', 'contact_phone_number', 'doctors')

        datetime = serializers.DateTimeField()
        reason = serializers.CharField()
        new_patient = serializers.BooleanField()
        contact_phone_number = serializers.CharField()
        doctors = DoctorSerializer(many=True)
