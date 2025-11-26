import uuid
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import time
from .models import Center
class CenterModelTest(TestCase):
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
    def test_center_creation(self):
        """Check that a Center instance is created correctly"""
        self.assertIsInstance(self.center, Center)
        self.assertEqual(self.center.center_name, "Test Clinic")
        self.assertEqual(self.center.center_type, "clinic")
        self.assertEqual(self.center.address, "123 Main St, Test City")
        self.assertEqual(self.center.latitude, 37.7749)
        self.assertEqual(self.center.longitude, -122.4194)
        self.assertEqual(self.center.contact_number, "123-456-7890")
        self.assertEqual(self.center.operational_status, "Open")
        self.assertEqual(self.center.opening_time, time(9, 0))
        self.assertEqual(self.center.closing_time, time(17, 0))
        self.assertEqual(str(self.center), "Test Clinic")
    def test_center_id_is_uuid(self):
        """Ensure the primary key is a UUID"""
        self.assertIsInstance(self.center.center_id, uuid.UUID)
    def test_default_address(self):
        """Check that address defaults to 'unknown' if not provided"""
        image_file = SimpleUploadedFile("test_image2.jpg", b"file_content", content_type="image/jpeg")
        default_center = Center.objects.create(
            center_name="Default Address Clinic",
            center_type="clinic",
            image_path=image_file,
            contact_number="987-654-3210",
            operational_status="Closed",
            opening_time=time(8, 0),
            closing_time=time(16, 0),
        )
        self.assertEqual(default_center.address, "unknown")
    def test_default_latitude_longitude(self):
        """Check that latitude and longitude default to 0.0"""
        image_file = SimpleUploadedFile("test_image3.jpg", b"file_content", content_type="image/jpeg")
        default_center = Center.objects.create(
            center_name="Default Lat Lon Clinic",
            center_type="counseling_center",
            image_path=image_file,
            contact_number="555-555-5555",
            operational_status="Open",
            opening_time=time(10, 0),
            closing_time=time(18, 0),
        )
        self.assertEqual(default_center.latitude, 0.0)
        self.assertEqual(default_center.longitude, 0.0)









