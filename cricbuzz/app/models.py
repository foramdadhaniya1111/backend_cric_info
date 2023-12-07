from django.db import models

# Create your models here.
class player_info(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField()
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    
class icc_bowling(models.Model):
    position = models.IntegerField()
    rating = models.IntegerField()
    series =models.CharField(max_length=50)
    player = models.ForeignKey(player_info,on_delete=models.CASCADE,auto_created=True)
    
class icc_batting(models.Model):
    position = models.IntegerField()
    rating = models.IntegerField()
    series =models.CharField(max_length=50)
    player = models.ForeignKey(player_info,on_delete=models.CASCADE,auto_created=True)
    
class icc_all_rounder(models.Model):
    position = models.IntegerField()
    rating = models.IntegerField()
    series =models.CharField(max_length=50)
    player = models.ForeignKey(player_info,on_delete=models.CASCADE,auto_created=True)
    

    
