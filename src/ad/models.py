from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

AD_CONDITION =(
    ('New','New'),
    ('Like New','Like New'),
    ('Good Condition','Good Condition'),
    ('Bad Condition','Bad Condition'),
)
class Ad(models.Model):
    code = models.CharField(max_length=12,null=True, blank=True)
    owner = models.ForeignKey(User,related_name='ad_owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ad/')
    content = models.TextField(blank=True, null=0)
    price = models.IntegerField(default=1)
    category = models.ForeignKey('Category',limit_choices_to={'main_category__isnull':True},related_name='ad_category', on_delete=models.CASCADE)
    condition = models.CharField(max_length=15,choices=AD_CONDITION,null=True, blank=True)
    brand = models.ForeignKey('Brand',related_name='add_brand',null=True, blank=True, on_delete=models.CASCADE)

    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.code = '##'+((str(self.id)).center(10,'0'))
        super(Ad,self).save(*args, **kwargs)

class AdImages(models.Model):
    ad =models.ForeignKey(Ad, related_name="ad_images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ad_images/')

class Category(models.Model):
    name = models.CharField(max_length=50)
    main_category = models.ForeignKey('self',limit_choices_to={'main_category':None},related_name='maincategory', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name