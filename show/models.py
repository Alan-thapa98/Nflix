from django.db import models

# Create your models here.


class flix(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20000, default="")
    bio = models.CharField(max_length=20000, default="")
    hero = models.CharField(max_length=20000, default="")
    heroin = models.CharField(max_length=20000, default="")
    Movie = models.FileField(upload_to="video/Videos",
                             default="", max_length=5000)
    flix_poster = models.ImageField(upload_to='flix_poster', default="0")
    diacter = models.CharField(max_length=20000, default="")
    studio_name = models.CharField(max_length=20000, default="")
    categorys = models.CharField(max_length=20000, default="")
    tags = models.CharField(max_length=20000, default="")
    date_of_relese = models.IntegerField(default="0")
    views = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name

    # -- comments
    # -- likes and dislikes
    # -- replys
