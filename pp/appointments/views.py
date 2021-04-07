from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from django.shortcuts import get_object_or_404
from .serializers import AppointmentSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment


class GetDeleteUpdateAppointments(RetrieveUpdateAPIView):
    def get(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

    def put(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        appointment = Appointment.objects.get(pk=pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetPostAppointments(ListCreateAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()