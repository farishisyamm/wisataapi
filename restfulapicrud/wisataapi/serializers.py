from rest_framework import serializers
from .models import Wisata

class WisataSerializer(serializers.ModelSerializer):
    class Meta():
        model = Wisata
        fields = "__all__"
        