from django.db import models
from django.core.exceptions import ValidationError

import re

REGEX_MAX_LENGTH = 256

class RegexCharField(models.CharField):

    description = "A CharField holding a regular expression"

    def validate(self, value, model_instance):
        try:
            re.compile(value)
        except:
            raise ValidationError("Could not compile pattern into a regular expression")

