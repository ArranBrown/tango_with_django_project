from django.contrib import admin
from rango.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)

# Register your models here.

admin.site.register(Page, PageAdmin)

# Add in this class to customise the Admin Interface
