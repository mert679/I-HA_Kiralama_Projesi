from rest_framework import serializers
from .models import RentRecord


class RentRecordListSerializer(serializers.ModelSerializer):
    user_rent = serializers.CharField(read_only=True)
    iha = serializers.CharField(read_only=True)
    class Meta:
        model = RentRecord
        fields = '__all__'

