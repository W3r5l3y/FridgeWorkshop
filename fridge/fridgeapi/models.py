from django.db import models


class AmountType(models.Model):
    name = models.CharField(max_length=50, primary_key=True)


class ItemType(models.Model):
    unique_barcode = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=50)
    amount_type = models.ForeignKey(AmountType, on_delete=models.CASCADE)


class ShoppingList(models.Model):
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE, primary_key=True)
    amount = models.FloatField()


class IndividualItems(models.Model):
    id = models.AutoField(primary_key=True)
    expiration_date = models.DateField()
    type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    amount = models.FloatField()
