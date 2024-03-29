# Generated by Django 5.0.1 on 2024-01-16 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shortener", "0003_alter_shortenertable_expiry_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="shortenertable",
            name="qr_code",
            field=models.CharField(default="", max_length=10000),
        ),
        migrations.AlterField(
            model_name="shortenertable",
            name="expiry_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 19, 16, 56, 59, 596031, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
