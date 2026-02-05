from advertisements.serializers import AdvertisementSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.viewsets import ModelViewSet
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.models import Advertisement
from advertisements.filters import AdvertisementFilter
from django_filters.rest_framework import DjangoFilterBackend


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnly()]

        return []