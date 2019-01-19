# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Challenge

# Create your views here.
def challenges_list(request):
    MAX_OBJECTS = 20
    challenges = Challenge.objects.all()[:MAX_OBJECTS]
    data = {"challenges": list(challenges.values("question", "created_by", "pub_date"))}
    return JsonResponse(data)

def challenges_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    data = {"challenge": {
      "question": challenge.question,
      "created_by": challenge.created_by,
      "pub_date": challenge.pub_date
    }}
    return JsonResponse(data)