from django.db import models
from django.contrib import auth
from django.urls import reverse
from django.conf import settings
# Create your models here.
class LandBuy(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    image = models.ImageField(blank=True,null=True,upload_to='Buyimages/')
    discription = models.TextField()
    size = models.IntegerField(blank=True,null=True,default=0)
    def __str__(self):
        return self.name
        def get_absolute_url(self):
            return reverse('accounts:buy',kwargs={'username':self.user.username,'pk':self.pk})
class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return self.username
###################


class LandSellModel(models.Model):
    post_by = models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
    Property_name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    image = models.ImageField(null=True,blank=True,upload_to='images',default='D:\atom projects\webnew\web1\media\images\IMG_20190625_192316.jpg')
    discription = models.TextField()
    size = models.IntegerField(blank=True,null=True,default=0)
    def __str__(self):
        return self.Property_name
    def get_absolute_url(self):
        return reverse('accounts:sell',kwargs={'username':self.user.username,'pk':self.pk})
