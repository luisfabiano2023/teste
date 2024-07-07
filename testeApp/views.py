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
    serializer = infoSerializer(data=request.data)
    
    # Check if the data already exists
    if info.objects.filter(**request.data).exists():
        return Response({'error': 'This data already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def update(request, pk):
    try:
        info = info.objects.get(pk=pk)
        serializer = infoSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except info.DoesNotExist:
        return Response({'error': 'Info not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def read(request):
    infos = info.objects.all()  # retrieve all existing Info objects
    serializer = infoSerializer(infos, many=True)  # serialize the data
    return Response(serializer.data)  # return the serialized data