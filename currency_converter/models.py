import uuid

from django.db import models


# Create your models here.
class CurrencyConversion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    base_currency = models.CharField(max_length=30, unique=True, blank=True, null=True)
    target_currency = models.CharField(max_length=30, unique=True, blank=True, null=True)
    rate = models.DecimalField(decimal_places=10, max_digits=10, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "tbl_currency_conversion"
