from django.shortcuts import render
from services.models import Service
from rest_framework.response import Response
from users.models import User
from appointment.models import Appointment
from arv.models import ARVAvailability
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate
from .serializers import (
    ARVAvailabilitySerializer,
    UserSerializer,
    LoginSerializer,
    AppointmentSerializer,
    CenterSerializer,
    UserLocationSerializer,
    ServiceSerializer,
)
from rest_framework import viewsets, permissions, generics, status, filters
from center.models import Center
from location.models import UserLocation


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data["phone_number"]
        password = serializer.validated_data["password"]

        user = authenticate(request, username=phone_number, password=password)
        if not user:
            return Response(
                {"error": "Invalid phone number or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user_id": str(user.user_id),
                "user_type": user.user_type,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone_number": user.phone_number,
            }
        )


class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Center.objects.filter(center_type="clinic")
    serializer_class = CenterSerializer


class CounselingCenterViewSet(viewsets.ModelViewSet):
    queryset = Center.objects.filter(center_type="counseling_center")
    serializer_class = CenterSerializer


class CenterViewSet(viewsets.ModelViewSet):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer


class UserLocationViewSet(viewsets.ModelViewSet):
    queryset = UserLocation.objects.all()
    serializer_class = UserLocationSerializer


class NearbyCenterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer


class ARVAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = ARVAvailability.objects.all()
    serializer_class = ARVAvailabilitySerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
