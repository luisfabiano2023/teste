from urllib import request
from django.shortcuts import render
from .serializers import infoSerializer
from .models import info
from . import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
def create_info(request):
    serializer = InfoSerializer(data=request.data)
    
    # Check if the data already exists
    if Info.objects.filter(**request.data).exists():
        return Response({'error': 'This data already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




@api_view(['POST'])
def update():
    pass
@api_view(['GET'])
def read():
    pass