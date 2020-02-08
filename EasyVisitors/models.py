from django.db import models

# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=300, verbose_name='Counter Name')
    counter = models.DecimalField(max_digits=10, decimal_places=0,verbose_name="Visitor Counter",default=1)
    def __str__(self):
        return self.name
