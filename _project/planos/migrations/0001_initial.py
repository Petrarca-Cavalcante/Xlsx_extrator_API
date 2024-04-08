# Generated by Django 5.0.4 on 2024-04-08 15:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("vidas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Plano",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("nome", models.CharField(max_length=25)),
                ("servicos", models.TextField(max_length=300)),
                ("valor", models.DecimalField(decimal_places=2, max_digits=10)),
                ("dependentes", models.IntegerField(default=0)),
                (
                    "vidas",
                    models.ManyToManyField(related_name="planos", to="vidas.vida"),
                ),
            ],
        ),
    ]
