# Generated by Django 3.1.4 on 2020-12-20 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]