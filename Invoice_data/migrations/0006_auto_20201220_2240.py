# Generated by Django 3.1.4 on 2020-12-20 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice_data', '0005_auto_20201220_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoices',
            old_name='invioce_number',
            new_name='invoice_number',
        ),
    ]
