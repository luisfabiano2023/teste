from django.shortcuts import render
from .serializers import infoSerializer
from .models import info
from . import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
def create():
    item = infoSerializer(data=request.data)
 
    # validating for already existing data
    if info.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    pass




@api_view(['POST'])
def update():
    pass
@api_view(['GET'])
def read():
    pass