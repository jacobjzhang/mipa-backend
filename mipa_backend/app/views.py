# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import generics

from .models import Challenge, Question
from .serializers import ChallengeSerializer, QuestionSerializer

# Create your views here.
class challenges_list(generics.ListAPIView):
    MAX_OBJECTS = 20
    queryset = Challenge.objects.all()[:MAX_OBJECTS]
    serializer_class = ChallengeSerializer

class challenges_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

class questions_list(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class questions_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
