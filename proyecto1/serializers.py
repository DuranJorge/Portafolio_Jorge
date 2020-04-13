from rest_framework import serializers
from proyecto1.models import Historia
class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        """fields = ('id', 'email', 'title', 'description')"""
        fields = '__all__'