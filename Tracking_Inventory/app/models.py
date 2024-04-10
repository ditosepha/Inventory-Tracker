from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=25)
    serial_number = models.CharField(max_length=15)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        db_table = "ITEMS DATA"