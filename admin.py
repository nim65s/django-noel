from django.contrib.admin import ModelAdmin, site

from .models import ChristmasGroup

site.register(ChristmasGroup)
