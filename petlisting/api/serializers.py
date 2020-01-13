from ..models import Petlisting
from rest_framework import serializers


class PetSerializer(serializers.ModelSerializer):
    interested_pets = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Petlisting
        fields = ('pet', 'name', 'breed', 'gender', 'location', 'about', 'interested_pets')
        # exclude = ('date_listed',)

class PetImageSerializer(serializers.Serializer):
    
    class Meta:
        model = Petlisting
        fields = ('pet_image',)