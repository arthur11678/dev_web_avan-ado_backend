from django.db import models
from .Product import Product

class Drink(models.Model):
    id = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    volume = models.IntegerField()
    type = models.CharField(max_length=22)
    
    def __str__(self):
        return str(self.id_product.name)
    
    class Meta:
        db_table = 'drink'
        managed = True
        verbose_name = 'Drink'
        verbose_name_plural = 'Drinks'
        ordering = ["-id"]