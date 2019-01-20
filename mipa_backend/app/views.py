# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Challenge, Question, Profile
from .serializers import ChallengeSerializer, QuestionSerializer, ProfileSerializer

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

@api_view(['GET', 'PUT', 'DELETE'])
def profile_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        profile = Profile.objects.get(pk=pk)
    except profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)