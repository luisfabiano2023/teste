from django.db.models import fields
from rest_framework import serializers
from .models import info

class infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = info
        fields = ('id','nivel_dagua','mensagem','data_hora','status')