"""StudyBuddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from rest_framework import routers
from groupfinder import views

router = routers.SimpleRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accountmanager.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    
    path('studygroups/', views.StudyGroupList.as_view()),
    path('studygroups/<int:pk>/update', views.StudyGroupUpdate.as_view()),
    path('studygroups/<int:pk>/comments', views.GetStudyGroupComments.as_view()),
    path('amenities', views.AmenityList.as_view()),
    path('locations', views.LocationsGet.as_view()),
    path('locations/<int:pk>/update', views.LocationUpdate.as_view()),
    path('locations/add', views.LocationAdd.as_view()),
    path('users/', views.UserList.as_view()),
]
