from django.db import models
import random
# Create your models here.

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254, null=True, blank=True, default="@amb.sch.ae")
    number = models.CharField(max_length=15, blank=True, null=True, default="05") 
    role = models.CharField(max_length=40)
    about = models.TextField()
    photo = models.ImageField(upload_to='board_photos/')
    
class FAQ(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()  
    
class Chair(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254, default="@amb.sch.ae")
    about = models.TextField()
    photo = models.ImageField(upload_to='chair_photos/')
    
class Committee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    about = models.TextField()
    photo = models.ImageField(upload_to='committee_photos/')
    topic = models.TextField()
    chair_1_id = models.ForeignKey(Chair, on_delete=models.CASCADE, related_name='chair_1_committees')
    chair_2_id = models.ForeignKey(Chair, on_delete=models.CASCADE, related_name='chair_2_committees')
    chair_3_id = models.ForeignKey(Chair, on_delete=models.CASCADE, related_name='chair_3_committees', null=True, blank=True)
    background_guide = models.FileField(upload_to="background_guide", max_length=254, default='background_guide/default.pdf')

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=10000, default="")
    album_description = models.CharField(max_length=10000, default="")
    cover_photo = models.ImageField(upload_to='album_cover_photos/', default="album_cover_photos/placeholder.webp")
class MediaItem(models.Model):
    id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='gallery/', null=True, blank=True, default="album_cover_photos/placeholder.webp")
    video = models.URLField(max_length=10000, default="https://www.youtube.com/embed/dQw4w9WgXcQ?si=jijqIduCfHYCQETv", null=True, blank=True)
    media_type = models.CharField(max_length=70,choices=[("video", "Video"),("image", "Photo")], default="image")
    description = models.CharField(max_length=10000, default="")
    description_visibility = models.CharField(max_length=10000, choices=[("none", "Hidden"), ("block", "Shown")], default="block")
    album = models.ForeignKey(Album, related_name='media_items', on_delete=models.CASCADE)

class Misc(models.Model):
    # id = models.AutoField(primary_key=False)
    Key = models.CharField(max_length=1000, default=str(random.randint(0, 999999)), primary_key=True)
    
    Value = models.CharField(max_length=500000, default="")
    @classmethod
    def get_label(cls, key):

        """Get the value of a label via key.
        If not found, create one with the default value in
        settings.LABELS."""

        try:
            return cls.objects.get(key=key).value
        except:
            default_value = str(random.randint(0, 999999))
            cls.objects.create(key=key, value=default_value)
            return default_value

class ScheduleEntry(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    event_title = models.CharField(max_length=10000)