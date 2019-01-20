from rest_framework import serializers
from . import models

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "challenge", "kind", "question", "code", "options", "solution", "hint", "category", "questionImage", "hintImage", "created_at",)
        model = models.Question

class ChallengeSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        fields = ("id", "title", "category", "difficulty", "questions", "created_at",)
        model = models.Challenge

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("user", "bio", "location", "current_score",)
        model = models.Profile
