# Generated by Django 3.0.3 on 2020-06-05 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200605_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landbuy',
            name='image',
            field=models.ImageField(default='D:\x07tom projects\\webnew\\web1\\media\\images\\IMG_20191102_173526.jpg', upload_to='Buyimages/% Y/% m/% d/'),
        ),
    ]