# Generated by Django 4.1.4 on 2024-05-21 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_alter_misc_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='misc',
            name='Key',
            field=models.CharField(default='530442', max_length=1000, primary_key=True, serialize=False),
        ),
    ]
