from django.urls import path
from backend_flutter.views import *

urlpatterns = [
  path('', Home.as_view(), name='home'),
]