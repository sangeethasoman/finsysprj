# Generated by Django 4.0.4 on 2022-12-06 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0053_alter_purchasebill_grand_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='grandtotal',
            field=models.FloatField(default=0, null=True),
        ),
    ]
