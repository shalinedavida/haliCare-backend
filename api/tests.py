from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.test import TestCase
from arv.models import ARVAvailability
from datetime import datetime
import datetime
from appointment.models import Appointment

User = get_user_model()


class UserAuthTests(APITestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.profile_url = reverse("profile")
        self.user_data = {
            "first_name": "Ahmed",
            "last_name": "Ali",
            "phone_number": "0712345678",
            "password": "mypassword",
            "user_type": "PATIENT",
        }

    def test_user_can_register(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            User.objects.filter(phone_number=self.user_data["phone_number"]).exists()
        )

    def test_user_can_login_and_get_token(self):
        User.objects.create_user(
            phone_number=self.user_data["phone_number"],
            password=self.user_data["password"],
            first_name="John",
            last_name="Doe",
            user_type="PATIENT",
        )
        response = self.client.post(
            self.login_url,
            {
                "phone_number": self.user_data["phone_number"],
                "password": self.user_data["password"],
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

    def test_access_profile_requires_authentication(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_can_access_profile_with_token(self):
        self.client.post(self.register_url, self.user_data, format="json")
        login_response = self.client.post(
            self.login_url,
            {
                "phone_number": self.user_data["phone_number"],
                "password": self.user_data["password"],
            },
            format="json",
        )
        token = login_response.data["token"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        response = self.client.get(self.profile_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["phone_number"], self.user_data["phone_number"])


class AppointmentCRUDTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            phone_number="0711111111",
            first_name="Shir",
            last_name="Ley",
            user_type=User.UserType.PATIENT,
            password="akira2025",
        )
        self.client.force_authenticate(user=self.user)
        self.appointment_data = {
            "booking_status": "Upcoming",
            "appointment_date": "2025-09-10T00:00:00Z",
        }
        self.appointment = Appointment.objects.create(
            user_id=self.user,
            booking_status="Upcoming",
            appointment_date=datetime.date(2023, 12, 25),
        )

    def test_create_appointment(self):
        url = reverse("appointment-list")
        response = self.client.post(url, self.appointment_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_appointment_list(self):
        url = reverse("appointment-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_appointment_detail(self):
        url = reverse(
            "appointment-detail", kwargs={"pk": self.appointment.appointment_id}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["booking_status"], "Upcoming")

    def test_update_appointment(self):
        url = reverse(
            "appointment-detail", kwargs={"pk": self.appointment.appointment_id}
        )
        updated_data = {"booking_status": "Completed"}
        response = self.client.patch(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.appointment.refresh_from_db()
        self.assertEqual(self.appointment.booking_status, "Completed")

    def test_delete_appointment(self):
        url = reverse(
            "appointment-detail", kwargs={"pk": self.appointment.appointment_id}
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Appointment.objects.count(), 0)
