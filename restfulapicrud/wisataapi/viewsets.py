from rest_framework import viewsets
from . import models
from . import serializers

class WisataViewset(viewsets.ModelViewSet):
    queryset = models.Wisata.objects.all()
    serializer_class = serializers.WisataSerializer
    