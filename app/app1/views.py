from django.shortcuts import render
from app.app1.models import Model1

from app.app1.serializers import Model1Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class Model1List(APIView):
    def get(self, request, format=None):
        model1 = Model1.objects.all()
        serializer = Model1Serializer(model1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Model1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
