from django.contrib import admin

from .models import BakedGood, Ingredient

admin.site.register([BakedGood, Ingredient])
