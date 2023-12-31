# Generated by Django 4.2.6 on 2023-10-31 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('sub_title', models.CharField(blank=True, max_length=255)),
                ('picture', models.ImageField(blank=True, upload_to='portfolio/pictures/%Y/%m/%d')),
                ('picture_title', models.CharField(blank=True, max_length=255)),
                ('picture_sub_title', models.CharField(blank=True, max_length=255)),
                ('detail_title', models.CharField(blank=True, max_length=255)),
                ('detail_sub_title', models.CharField(blank=True, max_length=255)),
                ('detail_picture', models.ImageField(blank=True, upload_to='portfolio/detail_picture/%Y/%m/%d')),
                ('detail_description', models.TextField(blank=True)),
                ('detail_client', models.CharField(blank=True, max_length=255)),
                ('detail_category', models.CharField(blank=True, max_length=255)),
                ('picture_2', models.ImageField(blank=True, upload_to='portfolio/pictures_2/%Y/%m/%d')),
                ('picture_title_2', models.CharField(blank=True, max_length=255)),
                ('picture_sub_title_2', models.CharField(blank=True, max_length=255)),
                ('detail_title_2', models.CharField(blank=True, max_length=255)),
                ('detail_sub_title_2', models.CharField(blank=True, max_length=255)),
                ('detail_picture_2', models.ImageField(blank=True, upload_to='portfolio/detail_picture_2/%Y/%m/%d')),
                ('detail_description_2', models.TextField(blank=True)),
                ('detail_client_2', models.CharField(blank=True, max_length=255)),
                ('detail_category_2', models.CharField(blank=True, max_length=255)),
                ('picture_3', models.ImageField(blank=True, upload_to='portfolio/pictures_3/%Y/%m/%d')),
                ('picture_title_3', models.CharField(blank=True, max_length=255)),
                ('picture_sub_title_3', models.CharField(blank=True, max_length=255)),
                ('detail_title_3', models.CharField(blank=True, max_length=255)),
                ('detail_sub_title_3', models.CharField(blank=True, max_length=255)),
                ('detail_picture_3', models.ImageField(blank=True, upload_to='portfolio/detail_picture_3/%Y/%m/%d')),
                ('detail_description_3', models.TextField(blank=True)),
                ('detail_client_3', models.CharField(blank=True, max_length=255)),
                ('detail_category_3', models.CharField(blank=True, max_length=255)),
                ('picture_4', models.ImageField(blank=True, upload_to='portfolio/pictures_4/%Y/%m/%d')),
                ('picture_title_4', models.CharField(blank=True, max_length=255)),
                ('picture_sub_title_4', models.CharField(blank=True, max_length=255)),
                ('detail_title_4', models.CharField(blank=True, max_length=255)),
                ('detail_sub_title_4', models.CharField(blank=True, max_length=255)),
                ('detail_picture_4', models.ImageField(blank=True, upload_to='portfolio/detail_picture_4/%Y/%m/%d')),
                ('detail_description_4', models.TextField(blank=True)),
                ('detail_client_4', models.CharField(blank=True, max_length=255)),
                ('detail_category_4', models.CharField(blank=True, max_length=255)),
                ('picture_5', models.ImageField(blank=True, upload_to='portfolio/pictures_5/%Y/%m/%d')),
                ('picture_title_5', models.CharField(blank=True, max_length=255)),
                ('picture_sub_title_5', models.CharField(blank=True, max_length=255)),
                ('detail_title_5', models.CharField(blank=True, max_length=255)),
                ('detail_sub_title_5', models.CharField(blank=True, max_length=255)),
                ('detail_picture_5', models.ImageField(blank=True, upload_to='portfolio/detail_picture_5/%Y/%m/%d')),
                ('detail_description_5', models.TextField(blank=True)),
                ('detail_client_5', models.CharField(blank=True, max_length=255)),
                ('detail_category_5', models.CharField(blank=True, max_length=255)),
                ('picture_6', models.ImageField(blank=True, upload_to='portfolio/pictures_6/%Y/%m/%d')),
                ('picture_title_6', models.CharField(blank=True, max_length=255)),
                ('picture_sub_title_6', models.CharField(blank=True, max_length=255)),
                ('detail_title_6', models.CharField(blank=True, max_length=255)),
                ('detail_sub_title_6', models.CharField(blank=True, max_length=255)),
                ('detail_picture_6', models.ImageField(blank=True, upload_to='portfolio/detail_picture_6/%Y/%m/%d')),
                ('detail_description_6', models.TextField(blank=True)),
                ('detail_client_6', models.CharField(blank=True, max_length=255)),
                ('detail_category_6', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
            },
        ),
    ]
