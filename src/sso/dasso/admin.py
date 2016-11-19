from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import Ressource


class RessourceAdmin(GuardedModelAdmin):
    pass


admin.site.register(Ressource, RessourceAdmin)
