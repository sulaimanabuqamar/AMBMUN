# Generated by Django 4.1.4 on 2024-05-20 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_mediaitem_alter_misc_key_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='misc',
            name='Key',
            field=models.CharField(default='454792', max_length=1000, primary_key=True, serialize=False),
        ),
    ]