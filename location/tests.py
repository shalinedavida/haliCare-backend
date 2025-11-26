from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserLocation

User = get_user_model()


class UserLocationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            phone_number="1234567890",
            password="testpass",
            first_name="Test",
            last_name="User",
            user_type="Clinicians",
        )
        self.location = UserLocation.objects.create(
            user=self.user,
            address="456 Elm St, Nairobi City",
            latitude=12.345678,
            longitude=98.765432,
        )

    def test_userlocation_creation(self):
        self.assertIsInstance(self.location, UserLocation)
        self.assertEqual(self.location.user, self.user)
        self.assertEqual(self.location.address, "456 Elm St, Nairobi City")
        self.assertEqual(float(self.location.latitude), 12.345678)
        self.assertEqual(float(self.location.longitude), 98.765432)
        self.assertIsNotNone(self.location.created_at)

        self.assertEqual(
            str(self.location),
            f"{self.user.first_name} {self.user.last_name} ({self.user.phone_number}) at 456 Elm St, Nairobi City",
        )

    def test_null_address(self):
        location = UserLocation.objects.create(
            user=self.user,
            latitude=0.0,
            longitude=0.0,
        )
        self.assertIsNone(location.address)
        self.assertEqual(
            str(location),
            f"{self.user.first_name} {self.user.last_name} ({self.user.phone_number}) at Unknown",
        )

    def test_blank_latitude_longitude(self):
        location = UserLocation.objects.create(user=self.user, address="No LatLon")
        self.assertIsNone(location.latitude)
        self.assertIsNone(location.longitude)
        self.assertEqual(location.address, "No LatLon")
