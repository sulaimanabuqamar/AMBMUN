# Generated by Django 4.1.4 on 2024-05-20 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_misc_key'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gallery',
            new_name='Album',
        ),
        migrations.AlterField(
            model_name='misc',
            name='Key',
            field=models.CharField(default='571572', max_length=1000, primary_key=True, serialize=False),
        ),
    ]
