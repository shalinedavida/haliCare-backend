from django.db import models
from django.conf import settings


class UserLocation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "location_userlocation"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.phone_number}) at {self.address or 'Unknown'}"
