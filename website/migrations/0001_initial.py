# Generated by Django 5.0 on 2023-12-24 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=40)),
                ("email", models.EmailField(default="@amb.sch.ae", max_length=254)),
                (
                    "number",
                    models.CharField(
                        blank=True, default="05", max_length=15, null=True
                    ),
                ),
                ("role", models.CharField(max_length=40)),
                ("about", models.TextField()),
                (
                    "club",
                    models.CharField(
                        choices=[
                            ("AMIC", "Amic"),
                            ("AMRC", "Amrc"),
                            ("Executive Board", "Mun"),
                            ("None", "None"),
                        ],
                        default="None",
                        max_length=20,
                    ),
                ),
                ("photo", models.ImageField(upload_to="board_photos/")),
            ],
        ),
        migrations.CreateModel(
            name="Chair",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=40)),
                ("email", models.EmailField(default="@amb.sch.ae", max_length=254)),
                ("about", models.TextField()),
                ("photo", models.ImageField(upload_to="chair_photos/")),
            ],
        ),
        migrations.CreateModel(
            name="CoChair",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=40)),
                ("email", models.EmailField(default="@amb.sch.ae", max_length=254)),
                ("about", models.TextField()),
                ("photo", models.ImageField(upload_to="chair_photos/")),
            ],
        ),
        migrations.CreateModel(
            name="FAQ",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("question", models.TextField()),
                ("answer", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Committee",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=40)),
                ("about", models.TextField()),
                ("photo", models.ImageField(upload_to="committee_photos/")),
                ("topic_1", models.TextField()),
                ("topic_2", models.TextField()),
                (
                    "chair_1_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chair_1_committees",
                        to="website.chair",
                    ),
                ),
                (
                    "chair_2_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chair_2_committees",
                        to="website.chair",
                    ),
                ),
                (
                    "cochair_id",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cochair_committees",
                        to="website.chair",
                    ),
                ),
            ],
        ),
    ]
