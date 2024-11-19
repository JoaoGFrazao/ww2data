from rest_framework import serializers
from dados.models import WW2

class GeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = WW2
        fields = '__all__'