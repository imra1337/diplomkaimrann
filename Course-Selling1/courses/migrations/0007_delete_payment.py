# Generated by Django 4.2.9 on 2024-02-02 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_usercourse_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
