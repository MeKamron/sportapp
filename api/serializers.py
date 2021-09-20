from rest_framework import serializers
from main.models import SportCenter, SportTuri

class SportCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportCenter
        fields = ('nomi', "sport_turi", "manzil", "telfon", "latitude", "longtitude")


class SportTuriSerializer(serializers.ModelSerializer):
    sport_centers = SportCenterSerializer(many=True, read_only=True)
    class Meta:
        model = SportTuri
        fields = ('id','nomi', 'sport_centers')


