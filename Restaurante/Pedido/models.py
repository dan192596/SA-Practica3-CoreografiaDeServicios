from django.db import models

# Create your models here.
class Pedido(models.Model):    
    cui = models.CharField(max_length=100)
    status = models.IntegerField(default=0)    
    
    def __str__(self):
        return self.id