from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    icons = models.ImageField(upload_to='Service/icons/%Y/%m/%d', blank=True)
    icons_title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    icons_title_2 = models.CharField(max_length=255, blank=True)
    description_2 = models.TextField(blank=True)
    icons_title_3 = models.CharField(max_length=255, blank=True)
    description_3 = models.TextField(blank=True)
    


    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

           

