# Generated by Django 3.1.4 on 2021-11-07 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_payment_boat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='boat',
            new_name='animal_name',
        ),
    ]
