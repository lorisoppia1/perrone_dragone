from django.urls import path
from backend_flutter.views import *
from . import views

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('api/test/', Home.as_view(), name='api_test')
]