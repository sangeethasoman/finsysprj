# Generated by Django 4.2.1 on 2023-06-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0074_challan_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='challan',
            name='shipping',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='challanitem',
            name='discount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
