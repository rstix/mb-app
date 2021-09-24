from django.urls import path
from .views import HomePageVieW

urlpatterns = [
  path('',HomePageVieW.as_view(),name='home')
]
