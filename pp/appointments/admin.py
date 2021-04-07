from pp.appointments.models import Appointment
from django.contrib import admin


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'reason', 'new_patient', 'contact_phone_number')
    list_display_links = ['datetime', 'reason', 'new_patient', 'contact_phone_number']
    ordering = ['-id']
    sortable_by = ['datetime', 'reason', 'new_patient', 'contact_phone_number']
    save_on_top = True
    show_full_result_count = True
    search_fields = ['doctor__name']
