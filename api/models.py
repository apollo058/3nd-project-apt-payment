from django.db import models
from django.db.models.fields import CharField, DecimalField

class Payment(models.Model):
    name     = models.CharField(max_length=4)
    password = models.CharField(max_length=4)
    pay      = DecimalField(max_digits=8, decimal_places=1, default=0)

    class Meta:
        db_table = 'payment'
