# Generated by Django 5.0.1 on 2024-01-16 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shortener", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shortenertable",
            name="expiry_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 19, 16, 31, 6, 729807, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]