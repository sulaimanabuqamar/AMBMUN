# Generated by Django 4.1.4 on 2024-02-23 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_committee_background_guide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Misc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('MUN_Day_1', models.DateField()),
                ('MUN_Day_2', models.DateField()),
                ('MUN_Day_1_Registration_Start', models.TimeField()),
                ('MUN_Day_1_Registration_End', models.TimeField()),
                ('MUN_Day_1_Opening_Ceremony_Start', models.TimeField()),
                ('MUN_Day_1_Opening_Ceremony_End', models.TimeField()),
                ('MUN_Day_1_Committee_Session_1_Start', models.TimeField()),
                ('MUN_Day_1_Committee_Session_1_End', models.TimeField()),
                ('MUN_Day_1_Break_Start', models.TimeField()),
                ('MUN_Day_1_Break_End', models.TimeField()),
                ('MUN_Day_1_Committee_Session_2_Start', models.TimeField()),
                ('MUN_Day_1_Committee_Session_2_End', models.TimeField()),
                ('MUN_Day_2_Committee_Session_3_Start', models.TimeField()),
                ('MUN_Day_2_Committee_Session_3_End', models.TimeField()),
                ('MUN_Day_2_Break_Start', models.TimeField()),
                ('MUN_Day_2_Break_End', models.TimeField()),
                ('MUN_Day_2_Committee_Session_4_Start', models.TimeField()),
                ('MUN_Day_2_Committee_Session_4_End', models.TimeField()),
                ('MUN_Day_2_Closing_Ceremony_Start', models.TimeField()),
                ('MUN_Day_2_Closing_Ceremony_End', models.TimeField()),
            ],
        ),
    ]
