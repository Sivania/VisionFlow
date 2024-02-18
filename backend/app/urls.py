from django.urls import path
from .views import action

urlpatterns = [
    path('actions/', action, name='actions'),
]