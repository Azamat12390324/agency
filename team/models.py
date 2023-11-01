from django.db import models


class Team(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    picture = models.ImageField(upload_to='Team/picture/%Y/%m/%d', blank=True)
    name = models.CharField(max_length=255, blank=True)
    job = models.CharField(max_length=255, blank=True)


    picture_2 = models.ImageField(upload_to='Team/picture_2/%Y/%m/%d', blank=True)
    name_2 = models.CharField(max_length=255, blank=True)
    job_2 = models.CharField(max_length=255, blank=True)
    

    picture_3 = models.ImageField(upload_to='Team/picture_3/%Y/%m/%d', blank=True)
    name_3 = models.CharField(max_length=255, blank=True)
    job_3 = models.CharField(max_length=255, blank=True)
    

    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'teams'