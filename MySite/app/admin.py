from django.contrib import admin

# Register your models here.
from app.models import CarPicture, CarPictureInstance


# admin.site.register(CarPicture)
# admin.site.register(CarPictureInstance)
# Register the Admin classes for Book using the decorator
class CarPictureInline(admin.TabularInline):
    model = CarPictureInstance


@admin.register(CarPicture)
class CarPictureAdmin(admin.ModelAdmin):
    list_display = ('image', 'title')
    inlines = [CarPictureInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(CarPictureInstance)
class CarPictureInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('image', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
