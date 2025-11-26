import uuid
from center.models import Center
from django.db import models


class Service(models.Model):
    service_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    center_id = models.ForeignKey(Center, on_delete=models.CASCADE, null=True, blank=True)
    service_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service_name
