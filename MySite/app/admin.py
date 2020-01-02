from django.contrib import admin

# Register your models here.
from app.models import CarPicture, CarPictureInstance

admin.site.register(CarPicture)
admin.site.register(CarPictureInstance)