# Generated by Django 4.1.4 on 2024-05-29 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_mediaitem_media_type_mediaitem_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediaitem',
            name='photo',
            field=models.ImageField(blank=True, default='album_cover_photos/placeholder.webp', null=True, upload_to='gallery/'),
        ),
        migrations.AlterField(
            model_name='mediaitem',
            name='video',
            field=models.URLField(blank=True, default='https://www.youtube.com/embed/dQw4w9WgXcQ?si=jijqIduCfHYCQETv', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='misc',
            name='Key',
            field=models.CharField(default='736767', max_length=1000, primary_key=True, serialize=False),
        ),
    ]