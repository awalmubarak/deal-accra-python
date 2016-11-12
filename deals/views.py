from .serializers import DealSerializer
from .models import Deal
from rest_framework import viewsets


class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
