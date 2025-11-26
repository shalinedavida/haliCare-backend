from django.db import models
from users.models import User
from center.models import Center
from services.models import Service
import uuid


class Appointment(models.Model):
    BOOKING_STATUS_CHOICE = [
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
        ("Upcoming", "Upcoming"),
    ]
    appointment_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    center_id = models.ForeignKey(
        Center, on_delete=models.CASCADE, null=True, blank=True
    )
    service_id = models.ForeignKey(
        Service, on_delete=models.CASCADE, null=True, blank=True
    )
    booking_status = models.CharField(max_length=100, choices=BOOKING_STATUS_CHOICE)
    transfer_letter = models.ImageField(upload_to="uploads/", null=True, blank=True)
    appointment_date = models.DateTimeField()

    def __str__(self):
        return f"Appointment {self.appointment_id}"
