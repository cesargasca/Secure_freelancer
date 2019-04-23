'''modelos sf '''
from django.db import models


# Create your models here.


class Test(models.Model):
    '''modelo de prueba '''
    algo = models.CharField(max_length=50)
