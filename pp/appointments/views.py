from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from django.shortcuts import get_object_or_404
from .serializers import AppointmentSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment
from datetime import datetime


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

    def get_queryset(self):
        queryset = Appointment.objects.all()
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if start_date:
            try:
                start_date = datetime.strptime(start_date, '%m-%d-%Y')
            except ValueError as e:
                start_date = None

        if end_date:
            try:
                end_date = datetime.strptime(end_date, '%m-%d-%Y')
            except ValueError as e:
                end_date = None

        if start_date and end_date:
            return queryset.filter(datetime__range=(start_date, end_date))
        elif start_date:
            return queryset.filter(datetime__gte=start_date)
        elif end_date:
            return queryset.filter(datetime__lte=end_date)

        return queryset
