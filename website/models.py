from django.db import models

# Create your models here.

class Board(models.Model):
    class Club(models.TextChoices):
        AMIC = 'AMIC'
        AMRC = 'AMRC'
        MUN = 'Executive Board'
        NONE = 'None'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254, null=True, blank=True, default="@amb.sch.ae")
    number = models.CharField(max_length=15, blank=True, null=True, default="05") 
    role = models.CharField(max_length=40)
    about = models.TextField()
    club = models.CharField(max_length=20, choices=Club.choices, default=Club.NONE)
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
    
class CoChair(models.Model):
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
    cochair_id = models.ForeignKey(CoChair, on_delete=models.CASCADE, related_name='cochair_committees', null=True, blank=True)