from django.contrib import admin

from horses.models import Breed, Horse

# Register your models here.

admin.site.register(Breed)
admin.site.register(Horse)