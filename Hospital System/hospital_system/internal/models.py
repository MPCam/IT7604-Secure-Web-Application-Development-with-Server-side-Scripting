from django.db import models
from django.db.models import Q, F
from django.core.validators import MinValueValidator
import datetime

# Create your models here.


class Department(models.Model):
    department = models.CharField(max_length=20)
    head_doctor = models.ForeignKey('Doctor', on_delete=models.PROTECT, related_name='departments', blank=True, null=True)

    def __str__(self):
        return self.department

class Doctor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    department = models.ForeignKey('Department', on_delete=models.PROTECT, related_name='doctors', blank=True, null=True)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()

    def __str__(self):
        return f"DR {self.last_name}"

class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Appointment(models.Model):
    class AppointmentType(models.TextChoices):
        GENERAL = 'GENERAL', 'General Consultation'
        FOLLOW_UP = 'FOLLOW_UP', 'Follow-up'
        EMERGENCY = 'EMERGENCY', 'Emergency'
        SURGERY = 'SURGERY', 'Surgery'
        CHECKUP = 'CHECKUP', 'Routine Check-up'

    class Status(models.TextChoices):
        SCHEDULED = 'SCHEDULED', 'Scheduled'
        COMPLETED = 'COMPLETED', 'Completed'
        CANCELLED = 'CANCELLED', 'Cancelled'
        NO_SHOW = 'NO_SHOW', 'No Show'
        RESCHEDULED = 'RESCHEDULED', 'Rescheduled'
    
    TIME_SLOTS = [
        (datetime.time(hour=h), f"{h:02d}:00") for h in range(9, 17)
    ]

    appointment_code = models.CharField(max_length=20, unique=True, help_text='Unique appointment code, for example APT-2026-0001.',)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='appointments',)
    doctor = models.ForeignKey('Doctor', on_delete=models.PROTECT, related_name='appointments',)
    appointment_type = models.CharField(max_length=20, choices=AppointmentType.choices, default=AppointmentType.GENERAL,)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SCHEDULED,)
    appointment_date = models.DateField()
    start_time = models.TimeField(choices=TIME_SLOTS)
    end_time = models.TimeField(choices=TIME_SLOTS)
    room_number = models.CharField(max_length=10, blank=True,)
    reasons = models.CharField(max_length=255)
    symptoms = models.TextField(blank=True)
    diagnosis = models.TextField(blank=True)
    prescription = models.TextField(blank=True)
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])
    is_follow_up = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['appointment_date', 'start_time']
        constraints = [
            models.CheckConstraint(
                condition=Q(end_time__gt=F('start_time')),
                name = 'appointment_end_time_after_start_time',
            ),
            models.UniqueConstraint(
                fields=['doctor', 'appointment_date', 'start_time'],
                name='unique_doctor_time_slot_per_day',
            ),
        ]


    def __str__(self):
        return f'{self.appointment_code} - {self.patient} with {self.doctor}'