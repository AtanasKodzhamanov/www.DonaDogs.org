# Generated by Django 4.1.3 on 2022-11-12 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0041_dog_adoption_pic_after_1_dog_adoption_pic_after_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='adoption_country_bg',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='dog',
            name='adoption_country_eng',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
    ]
