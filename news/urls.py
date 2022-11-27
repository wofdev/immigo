from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from news import views

# router = routers.DefaultRouter()
# router.register('', views.NewsAPIView.as_view(), basename='dddd')

urlpatterns = [
    path('', views.NewsAPIView.as_view()),
]