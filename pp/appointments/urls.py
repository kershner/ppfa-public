from django.urls import path
from . import views 

app_name = 'appointments'

urlpatterns = [
    path('api/v1/appointments/',
        views.GetPostAppointments.as_view(),
        name="get_post_appointments"
    ),
    path('api/v1/appointments/<int:pk>',
        views.GetDeleteUpdateAppointments.as_view(),
        name="get_delete_update_appointments"
    ),
]