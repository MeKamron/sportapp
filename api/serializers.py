from rest_framework import serializers
from main.models import SportCenter, SportTuri


class SportTuriSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportTuri
        fields = ('nomi', )


class SportCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportCenter
        fields = ('nomi', "sport_turi", "manzil", "telfon", "latitude", "longtitude")