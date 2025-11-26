import csv
from django.core.management.base import BaseCommand
from center.models import Center


class Command(BaseCommand):
    help = "Import centers from CSV"

    def handle(self, *args, **options):
        with open("Counselling_Centers_for_Import_Version2.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                latitude = float(row.get("latitude") or 0.0)
                longitude = float(row.get("longitude") or 0.0)
                operating_hours = row.get("operating_hours", "Not Provided")
                center_name = Center.objects.filter(center_name=row["center_name"])
                if not center_name:
                    Center.objects.create(
                        center_name=row["center_name"],
                        center_type=row["center_type"],
                        image_path=row.get("image_path", ""),
                        address=row["address"],
                        latitude=latitude,
                        longitude=longitude,
                        contact_number=row.get("contact_number", ""),
                        operational_status=row.get("operational_status", ""),
                        operating_hours=operating_hours,
                    )
        self.stdout.write(self.style.SUCCESS("Centers imported successfully."))
