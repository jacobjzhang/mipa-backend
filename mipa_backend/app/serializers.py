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

class ChallengeCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "profile", "challenge", "points_received", "created_at",)
        model = models.ChallengeCompletion

class ProfileSerializer(serializers.ModelSerializer):
    challenge_completions = ChallengeCompletionSerializer(many=True, read_only=True)

    class Meta:
        fields = ("id", "user", "bio", "location", "current_score", "challenge_completions",)
        model = models.Profile
