# Generated by Django 4.0.4 on 2022-12-02 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0037_rename_transaction_profit_loss_transactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='profit_loss',
            name='pdebit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.purchasedebit'),
        ),
    ]
