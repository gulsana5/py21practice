
from django.urls import path, include

from .views import TemplateView


urlpatterns = [
    path('user/', TemplateView.as_view()),
]
