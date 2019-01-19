# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Challenge

# Create your views here.
def challenges_list(request):
    MAX_OBJECTS = 20
    challenges = Challenge.objects.all()[:MAX_OBJECTS]
    data = {"challenges": list(challenges.values("title", "category", "difficulty", "created_at"))}
    return JsonResponse(data)

def challenges_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    data = {"challenge": {
      "title": challenge.title,
      "category": challenge.category,
      "difficulty": challenge.difficulty,      
      "created_at": challenge.created_by
    }}
    return JsonResponse(data)