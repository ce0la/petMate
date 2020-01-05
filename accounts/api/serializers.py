from ..models import CustomUser
from ..forms import CustomUserCreationForm, CustomUserChangeForm
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'location')
