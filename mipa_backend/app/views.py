# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import generics

from .models import Challenge
from .serializers import ChallengeSerializer

# Create your views here.
class challenges_list(generics.ListAPIView):
    MAX_OBJECTS = 20
    queryset = Challenge.objects.all()[:MAX_OBJECTS]
    serializer_class = ChallengeSerializer

def challenges_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    data = {"challenge": {
      "title": challenge.title,
      "category": challenge.category,
      "difficulty": challenge.difficulty,      
      "created_at": challenge.created_by
    }}
    return JsonResponse(data)