from ..models import Petlisting
from rest_framework import serializers


class PetSerializer(serializers.ModelSerializer):
    interested_pets = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Petlisting
        fields = ('pet', 'name', 'breed', 'gender', 'location', 'about')
        # exclude = ('date_listed',)