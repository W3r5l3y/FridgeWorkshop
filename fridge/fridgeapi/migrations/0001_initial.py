# Generated by Django 5.1.5 on 2025-01-21 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AmountType',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('unique_barcode', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('amount_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridgeapi.amounttype')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('item_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fridgeapi.itemtype')),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='IndividualItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('expiration_date', models.DateField()),
                ('amount', models.FloatField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridgeapi.itemtype')),
            ],
        ),
    ]
