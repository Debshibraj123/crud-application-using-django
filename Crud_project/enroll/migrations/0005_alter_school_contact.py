# Generated by Django 4.1.5 on 2023-01-30 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0004_school_address_school_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='contact',
            field=models.CharField(max_length=100),
        ),
    ]
