from rest_framework import serializers
from appointment.models import Appointment
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from users.models import User
from center.models import Center
from location.models import UserLocation
from location.utils import geocode_address
from arv.models import ARVAvailability
from services.models import Service

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "user_id",
            "phone_number",
            "first_name",
            "last_name",
            "user_type",
            "password",
            "date_joined",
        ]
        read_only_fields = ["user_id", "date_joined"]

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain digits only.")
        if len(value) < 10 or len(value) > 15:
            raise serializers.ValidationError(
                "Phone number must be between 10 and 15 digits."
            )
        return value

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)


class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = "__all__"

    def create(self, validated_data):
        address = validated_data.get("address", "")
        if address:
            lat, lon = geocode_address(address)
            validated_data["latitude"] = lat
            validated_data["longitude"] = lon
        return super().create(validated_data)


class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = "__all__"

    def create(self, validated_data):
        address = validated_data.get("address", "")
        if address:
            lat, lon = geocode_address(address)
            validated_data["latitude"] = lat
            validated_data["longitude"] = lon
        return super().create(validated_data)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ARVAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ARVAvailability
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
