from django.contrib.admin import ModelAdmin, site

from .models import ChristmasGroup


class ChristmasAdmin(ModelAdmin):
    exclude = ('rotation',)

site.register(ChristmasGroup, ChristmasAdmin)
