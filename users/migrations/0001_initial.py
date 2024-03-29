# Generated by Django 5.0.2 on 2024-03-03 12:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserDetail",
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
                ("empcode", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50, null=True)),
                ("country", models.CharField(max_length=50, null=True)),
                ("contact", models.CharField(max_length=15, null=True)),
                ("gender", models.CharField(max_length=15, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
