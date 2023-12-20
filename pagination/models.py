from django.db import models

class Namelist(models.Model):
    name = models.CharField(max_length=32)
    classnumber = models.IntegerField()
    studentnumber = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name=verbose_name_plural="クラス名簿"
