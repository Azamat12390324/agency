from django.db import models
class Contact(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255,  blank=True)
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)
    site = models.URLField(blank=True)
    site_name = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


     
        

