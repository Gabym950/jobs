from rest_framework import serializers
from .models import Job
from .services import create_job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["id", "title", "description", "salary", "country", "status"]

    def create(self, validated_data):
        return create_job(**validated_data)
