from django.contrib import admin
from .models import Rental, Images, Location, Category

class ImageInline(admin.TabularInline):
    model = Images
    extra = 3

class RentalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                         {'fields': ['pub_date', 'title']}),
        ('House Description Details' , {'fields': ['house_detail', 'price', 'estate', 'image'], 'classes': ['collapse']}),
    ]

    list_display = ('title', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']

    search_fields = ['title']

    inlines = [ImageInline]


admin.site.register(Rental, RentalAdmin)
admin.site.register(Images)
admin.site.register(Location)
admin.site.register(Category)
