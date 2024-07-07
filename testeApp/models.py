from django.db import models
import datetime as dt

now= dt.datetime.now()
class info(models.Model):
    nivel_dagua = models.FloatField()
    mensagem=models.CharField(max_length=255)
    data_hora= now.strftime("%d/%m/%Y %H:%M:%S")
    status=models.BooleanField()
    def __str__(self):
        return self.mensagem
    

    