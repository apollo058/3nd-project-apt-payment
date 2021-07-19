from django.db import models

class Public(models.Model):
    name    = models.CharField(max_length=15)
    pwd     = models.CharField(max_length=200)
    payment = models.DecimalField(max_digits=8, decimal_places=1)

    class Meta:
        db_table = 'public'