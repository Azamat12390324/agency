from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    picture = models.ImageField(upload_to='portfolio/pictures/%Y/%m/%d', blank=True)
    picture_title = models.CharField(max_length=255, blank=True)
    picture_sub_title = models.CharField(max_length=255, blank=True)
    detail_title = models.CharField(max_length=255, blank=True)
    detail_sub_title = models.CharField(max_length=255, blank=True)
    detail_picture = models.ImageField(upload_to='portfolio/detail_picture/%Y/%m/%d', blank=True)
    detail_description = models.TextField(blank=True)
    detail_client = models.CharField(max_length=255, blank=True)
    detail_category = models.CharField(max_length=255, blank=True)



    picture_2 = models.ImageField(upload_to='portfolio/pictures_2/%Y/%m/%d', blank=True)
    picture_title_2 = models.CharField(max_length=255, blank=True)
    picture_sub_title_2 = models.CharField(max_length=255, blank=True)
    detail_title_2 = models.CharField(max_length=255, blank=True)
    detail_sub_title_2 = models.CharField(max_length=255, blank=True)
    detail_picture_2 = models.ImageField(upload_to='portfolio/detail_picture_2/%Y/%m/%d', blank=True)
    detail_description_2 = models.TextField(blank=True)
    detail_client_2 = models.CharField(max_length=255, blank=True)
    detail_category_2 = models.CharField(max_length=255, blank=True)



    picture_3 = models.ImageField(upload_to='portfolio/pictures_3/%Y/%m/%d', blank=True)
    picture_title_3 = models.CharField(max_length=255, blank=True)
    picture_sub_title_3 = models.CharField(max_length=255, blank=True)
    detail_title_3 = models.CharField(max_length=255, blank=True)
    detail_sub_title_3 = models.CharField(max_length=255, blank=True)
    detail_picture_3 = models.ImageField(upload_to='portfolio/detail_picture_3/%Y/%m/%d', blank=True)
    detail_description_3 = models.TextField(blank=True)
    detail_client_3 = models.CharField(max_length=255, blank=True)
    detail_category_3 = models.CharField(max_length=255, blank=True)



    picture_4 = models.ImageField(upload_to='portfolio/pictures_4/%Y/%m/%d', blank=True)
    picture_title_4 = models.CharField(max_length=255, blank=True)
    picture_sub_title_4 = models.CharField(max_length=255, blank=True)
    detail_title_4 = models.CharField(max_length=255, blank=True)
    detail_sub_title_4 = models.CharField(max_length=255, blank=True)
    detail_picture_4 = models.ImageField(upload_to='portfolio/detail_picture_4/%Y/%m/%d', blank=True)
    detail_description_4 = models.TextField(blank=True)
    detail_client_4 = models.CharField(max_length=255, blank=True)
    detail_category_4 = models.CharField(max_length=255, blank=True)


    picture_5 = models.ImageField(upload_to='portfolio/pictures_5/%Y/%m/%d', blank=True)
    picture_title_5 = models.CharField(max_length=255, blank=True)
    picture_sub_title_5 = models.CharField(max_length=255, blank=True)
    detail_title_5 = models.CharField(max_length=255, blank=True)
    detail_sub_title_5 = models.CharField(max_length=255, blank=True)
    detail_picture_5 = models.ImageField(upload_to='portfolio/detail_picture_5/%Y/%m/%d', blank=True)
    detail_description_5 = models.TextField(blank=True)
    detail_client_5 = models.CharField(max_length=255, blank=True)
    detail_category_5 = models.CharField(max_length=255, blank=True)


    picture_6 = models.ImageField(upload_to='portfolio/pictures_6/%Y/%m/%d', blank=True)
    picture_title_6 = models.CharField(max_length=255, blank=True)
    picture_sub_title_6 = models.CharField(max_length=255, blank=True)
    detail_title_6 = models.CharField(max_length=255, blank=True)
    detail_sub_title_6 = models.CharField(max_length=255, blank=True)
    detail_picture_6 = models.ImageField(upload_to='portfolio/detail_picture_6/%Y/%m/%d', blank=True)
    detail_description_6 = models.TextField(blank=True)
    detail_client_6 = models.CharField(max_length=255, blank=True)
    detail_category_6 = models.CharField(max_length=255, blank=True)






    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'


