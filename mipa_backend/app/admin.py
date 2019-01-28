# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Challenge, Question, Profile, ChallengeCompletion

# Register your models here.

class ChallengeAdmin(ImportExportModelAdmin):
    pass
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Question)
admin.site.register(Profile)
admin.site.register(ChallengeCompletion)