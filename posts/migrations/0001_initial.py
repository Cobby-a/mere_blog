# Generated by Django 4.2.4 on 2023-10-23 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Posts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("heading", models.CharField(max_length=100)),
                ("body", models.CharField(max_length=1000000)),
                ("date", models.DateTimeField(blank=True, default=datetime.datetime)),
            ],
        ),
    ]
