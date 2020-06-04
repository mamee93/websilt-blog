from django.contrib import admin
from  .models import Ad,AdImages,Category
# Register your models here.
admin.site.register(Ad)
admin.site.register(AdImages)
admin.site.register(Category)