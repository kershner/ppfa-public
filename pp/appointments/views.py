from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .serializers import AppointmentSerializer
from .models import Appointment

class GetDeleteUpdateAppointments(RetrieveUpdateAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self, pk):
        pass

    def get(self, request, pk):
        pass

    def post(self, request, pk):
        pass

    def delete(self, request, pk):
        pass

class GetPostAppointments(ListCreateAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        pass

    def get(self, request):
        pass

    def post(self, request):
        pass

    