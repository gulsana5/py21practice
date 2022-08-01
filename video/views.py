from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import VideoSerializer

class VideoAPIView(APIView):
    
    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Video created', status=200)
