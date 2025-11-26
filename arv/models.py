from django.db import models

from center.models import Center


class ARVAvailability(models.Model):
    Availability_CHOICES = [
        ("available", "Available"),
        ("not available", "Not available"),
    ]

    center = models.ForeignKey(Center, on_delete=models.CASCADE, null=True, blank=True)
    arv_availability = models.CharField(max_length=20, choices=Availability_CHOICES)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ARV Availability at {self.center_id}: {self.arv_availability}"
