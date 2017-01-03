from django.db import models
from .fields import RegexCharField

import re


class Ressource(models.Model):
    regex = RegexCharField(default=r'^$', max_length=256)
    manual_priority = models.PositiveSmallIntegerField(blank=True, default=0)
    public = models.BooleanField(default=False)
    any_authenticated = models.BooleanField(default=False)

    def __str__(self):
        return self.regex

    def matches(self, request):
        return re.fullmatch(self.regex, request)

    @property
    def priority(self):
        return self.manual_priority or self.regex.count('/')

    class Meta:
        permissions = (
            ('access_ressource', 'Access ressource'),
        )
