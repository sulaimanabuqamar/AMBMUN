# Generated by Django 5.0 on 2023-12-24 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0002_rename_topic_1_committee_topic_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="committee",
            name="cochair_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cochair_committees",
                to="website.cochair",
            ),
        ),
    ]
