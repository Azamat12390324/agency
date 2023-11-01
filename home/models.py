from collections.abc import Iterable
from django.db import models


class Home(models.Model):
    small_title = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    home_link = models.URLField(blank=True)
    home_link_name = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.small_title
    

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'
        
