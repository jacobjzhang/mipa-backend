"""mipa_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from .app.views import challenges_list, challenges_detail, questions_list, questions_detail, challenge_completion_list
from .app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path("challenges/", challenges_list.as_view()),
    path("challenges/<str:pk>/", challenges_detail.as_view()),
    path("questions/", questions_list.as_view()),
    path("questions/<int:pk>/", questions_detail.as_view()),
    path("profiles/<int:pk>/", views.profile_detail),
    path("challenge_completions/", challenge_completion_list.as_view())
]