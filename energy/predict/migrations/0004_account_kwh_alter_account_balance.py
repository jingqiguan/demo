# Generated by Django 4.1 on 2023-04-09 23:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("predict", "0003_transaction_action"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="kwh",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="account",
            name="balance",
            field=models.FloatField(default=0),
        ),
    ]
