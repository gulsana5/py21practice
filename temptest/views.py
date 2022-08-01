from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from django.contrib.auth import get_user_model


User = get_user_model()

class TemplateView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        user = User.objects.first()
        return Response({'user': user, 'car': '123456'})
