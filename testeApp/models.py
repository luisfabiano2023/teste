from django.db import models
import datetime as dt
class info(models.Model):
    mensagem=models.CharField(max_length=255)
    data_hora= dt.now()
    status=models.BooleanField()
    def __str__(self):
        return self.mensagem
    

    