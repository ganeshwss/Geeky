from django.urls import path, include
from geekyapp import views
from .views import *
# from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('transformers/',TransformerList.as_view(),name="transformers"),
    path('transformers/<int:pk>/',TransformerDetail.as_view(), name="transformers"),
]
