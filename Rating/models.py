from django.db import models
#from django.db.models import Avg
# Create your models here.
class Movies(models.Model):
    movie_name=models.CharField(max_length=100)
    release_date=models.DateField("date Released")
class Tvshows(models.Model):
    show_name=models.CharField(max_length=100)
    season=models.IntegerField
    episode=models.IntegerField
    release_date=models.DateField("Release date")

class Novels(models.Model):
    novel_name=models.CharField(max_length=100)
    writer=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)
    release_date = models.DateField("Release date")
class Ratings(models.Model):
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    tvshow=models.ForeignKey(Tvshows,on_delete=models.CASCADE)
    novels=models.ForeignKey(Novels,on_delete=models.CASCADE)
    rating=models.IntegerField(default=0)
    votes = models.IntegerField(default=0)