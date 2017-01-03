from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import Ressource


class RessourceAdmin(GuardedModelAdmin):
    list_display = ('regex', 'manual_priority', 'priority', 'public', 'any_authenticated')


admin.site.register(Ressource, RessourceAdmin)
