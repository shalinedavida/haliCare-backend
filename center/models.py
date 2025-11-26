import uuid
from django.db import models
from users.models import User

class Center(models.Model):
    CENTER_TYPE_CHOICES = [
        ("clinic", "Clinic"),
        ("counseling_center", "Counseling Center"),
    ]

    center_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    center_name = models.CharField(max_length=100, unique=True)
    center_type = models.CharField(max_length=100, choices=CENTER_TYPE_CHOICES)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image_path = models.ImageField(upload_to="uploads/", null=True, blank=True)
    address = models.CharField(max_length=50, blank=False, default="unknown")
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    contact_number = models.CharField(max_length=20)
    operational_status = models.CharField(max_length=50)
    opening_time = models.TimeField(blank=True, null=True)
    closing_time = models.TimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.center_name
