
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class Home(APIView):

  def get(self, request):
    response = {"ok": "ok"}
    return Response(response, status=status.HTTP_200_OK)
