from rest_framework import serializers
from . import models

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("title", "category", "difficulty", "created_at",)
        model = models.Challenge