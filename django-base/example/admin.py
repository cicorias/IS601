from django.contrib import admin

from .models import BakedGood, OtherBakedGood

admin.site.register(BakedGood)
admin.site.register(OtherBakedGood)
