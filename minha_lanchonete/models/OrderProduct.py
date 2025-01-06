from django.db import models
from .Order import Order
from .Product import Product

class OrderProduct(models.Model):
    id = models.AutoField(primary_key=True)
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_product.name)
    
    class Meta:
        db_table = 'order_product'
        managed = True
        verbose_name = 'OrderProduct'
        verbose_name_plural = 'OrderProducts'
        ordering = ["-id"]