from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    RegisterView,
    LoginView,
    ProfileView,
    CenterViewSet,
    NearbyCenterViewSet,
    ARVAvailabilityViewSet,
    ServiceViewSet,
    UserViewSet,
    AppointmentViewSet,
    ClinicViewSet,
    CounselingCenterViewSet,
)

from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r"appointment", AppointmentViewSet)
router.register(r"users", UserViewSet, basename="user")
router.register(r"centers", CenterViewSet, basename="center")
router.register(r"clinics", ClinicViewSet, basename="clinic")
router.register(
    r"counseling-centers", CounselingCenterViewSet, basename="counseling_center"
)
router.register(r"nearby-centers", NearbyCenterViewSet, basename="nearby_centers")

router.register(r"arvavailability", ARVAvailabilityViewSet, basename="arvailability")
router.register(r"services", ServiceViewSet, basename="services")


urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
