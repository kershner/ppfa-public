from pp.doctors.models import Doctor
from django.contrib import admin


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'rating')
    list_display_links = ['name', 'specialization', 'rating']
    ordering = ['-id']
    sortable_by = ['name', 'specialization', 'rating']
    list_filter = ['rating']
    save_on_top = True
    show_full_result_count = True
    search_fields = ['appointment']
