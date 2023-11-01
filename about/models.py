from django.db import models

class About(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    text_title = models.CharField(max_length=255, blank=True)
    text_sub_title = models.CharField(max_length=255, blank=True)
    text_description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='About/picture/%Y/%m/%d', blank=True)



    text_title_2 = models.CharField(max_length=255, blank=True)
    text_sub_title_2 = models.CharField(max_length=255, blank=True)
    text_description_2 = models.TextField(blank=True)
    picture_2 = models.ImageField(upload_to='About/picture_2/%Y/%m/%d', blank=True)


    text_title_3 = models.CharField(max_length=255, blank=True)
    text_sub_title_3 = models.CharField(max_length=255, blank=True)
    text_description_3 = models.TextField(blank=True)
    picture_3 = models.ImageField(upload_to='About/picture_3/%Y/%m/%d', blank=True)


    text_title_4 = models.CharField(max_length=255, blank=True)
    text_sub_title_4 = models.CharField(max_length=255, blank=True)
    text_description_4 = models.TextField(blank=True)
    picture_4 = models.ImageField(upload_to='About/picture_4/%Y/%m/%d', blank=True)
    


    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

        
