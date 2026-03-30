from django.contrib import admin
from .models import Appointment, Doctor, Patient, Department


# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Department)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'appointment_code',
        'patient',
        'doctor',
        'appointment_date',
        'start_time',
        'end_time',
        'appointment_type',
        'status',
        'consultation_fee',
        'is_follow_up',
    )
    list_filter = (
        'status',
        'appointment_type',
        'is_follow_up',
        'appointment_date',
        'doctor',
    ) 
    search_fields = (
        'appointment_code',
        'patient__first_name',
        'patient__last_name',
        'patient__patient_id',
        'doctor__first_name',
        'doctor__last_name',
        'doctor__doctor_id',
        'reasons',
        'room_number',
    )
    ordering = ('appointment_date', 'start_time', 'doctor__last_name')

    fieldsets = (
        ('Appointment Details', {
            'fields': (
                'appointment_code',
                'appointment_type',
                'status',
                'is_follow_up',
                'patient',
                'doctor',
                'appointment_date',
                ('start_time', 'end_time'),
                'room_number',
            )
        }),
        ('Clinical and Billing Information', {
            'fields': (
                'reasons',
                'symptoms',
                'diagnosis',
                'prescription',
                'consultation_fee'
            )
        }),
    )

