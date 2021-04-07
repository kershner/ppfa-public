from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('name', 'specialization', 'rating')

        name = serializers.CharField()
        specialization = serializers.CharField()
        rating = serializers.IntegerField()
