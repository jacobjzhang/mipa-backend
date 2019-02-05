# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pdb
import os

from .md_to_json import MdToJson
from .models import Challenge, Question, Profile, ChallengeCompletion
from .serializers import ChallengeSerializer, QuestionSerializer, ProfileSerializer, ChallengeCompletionSerializer

# Create your views here.
class challenges_list(generics.ListCreateAPIView):
    MAX_OBJECTS = 20
    queryset = Challenge.objects.all()[:MAX_OBJECTS]
    serializer_class = ChallengeSerializer

    def get(self, request, *args, **kwargs):
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, '../curriculum/challenges/')
        challenge_list = os.listdir(file_path)
        return Response(data=challenge_list, status=status.HTTP_200_OK) 

class challenges_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

    def get(self, request, *args, **kwargs):
        slug = kwargs['pk']
        data = MdToJson(slug).json_result()
        return Response(data=data, status=status.HTTP_200_OK)    

class questions_list(generics.ListCreateAPIView):
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

class challenge_completion_list(generics.ListCreateAPIView):
    queryset = ChallengeCompletion.objects.all()
    serializer_class = ChallengeCompletionSerializer

    def create(self, request, *args, **kwargs):
        profile = Profile.objects.get(pk=request.POST['profile'])
        new_score = profile.current_score + int(request.POST['points_received'])
        profile.current_score = new_score

        try:
          profile.save(update_fields=["current_score"])
          return super(challenge_completion_list, self).create(request, *args, **kwargs)
        except:
          return Response(status=status.HTTP_404_NOT_FOUND)