from django.db import models

# Create your models here.

class ProvCity(models.Model):
    abittle=models.CharField(max_length=20)
    aid=models.ForeignKey('self',null=True,blank=True)
    class Meta:
        db_table='booktest_areainfo'

