from django.urls import re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductsList

urlpatterns = [
    re_path(r'^', ProductsList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
