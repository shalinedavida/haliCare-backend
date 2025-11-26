import uuid
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from center.models import Center
from .models import ARVAvailability
from datetime import time
class ARVAvailabilityTest(TestCase):
    def setUp(self):
        image_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        self.center = Center.objects.create(
            center_name="Test Clinic",
            center_type="clinic",
            image_path=image_file,
            address="123 Main St, Test City",
            latitude=37.7749,
            longitude=-122.4194,
            contact_number="123-456-7890",
            operational_status="Open",
            opening_time=time(9, 0),
            closing_time=time(17, 0),
        )
    def test_arv_availability_creation(self):
        arv = ARVAvailability.objects.create(
            center=self.center,
            arv_availability="available",
        )
        expected_str = f"ARV Availability at {self.center.center_id}: available"
        self.assertEqual(str(arv), expected_str)
        self.assertEqual(arv.center, self.center)
        self.assertEqual(arv.arv_availability, "available")
        self.assertIsInstance(arv.center.center_id, uuid.UUID)











