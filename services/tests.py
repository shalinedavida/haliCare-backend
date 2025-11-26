from django.test import TestCase
from services.models import Service
import uuid


class ServiceModelTest(TestCase):
    def setUp(self):
        self.service = Service.objects.create(
            service_name="HIV Testing",
            status="Active",
            description="Free HIV Tests are offered every Wednesday",
        )

    def test_service_creation_and_attributes(self):
        retrieved_service = Service.objects.get(pk=self.service.pk)
        self.assertEqual(retrieved_service.service_name, "HIV Testing")
        self.assertEqual(retrieved_service.status, "Active")
        self.assertEqual(
            retrieved_service.description, "Free HIV Tests are offered every Wednesday"
        )
        self.assertIsInstance(retrieved_service, Service)

    def test_service_id_is_uuid(self):
        self.assertIsNotNone(self.service.service_id)
        self.assertIsInstance(self.service.service_id, uuid.UUID)

    def test_string_representation(self):
        self.assertEqual(str(self.service), "HIV Testing")

    def test_last_updated_auto_now(self):
        initial_time = self.service.last_updated
        self.service.service_name = "ARV Medication Service"
        self.service.save()
        updated_service = Service.objects.get(pk=self.service.pk)
        self.assertGreater(updated_service.last_updated, initial_time)
