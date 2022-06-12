from django.db import models

# Create your models here.
class Table(models.Model):
    table_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=100)

    def __str__(self):
        return self.table_name

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    table_id = models.IntegerField()
    order_time = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=100)
    order_price = models.FloatField()
    order_menu = models.CharField(max_length=100)



