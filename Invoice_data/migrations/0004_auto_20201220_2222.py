# Generated by Django 3.1.4 on 2020-12-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice_data', '0003_auto_20201220_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='digitized',
            field=models.BooleanField(default='undigitized'),
        ),
    ]
