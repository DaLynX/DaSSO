from django.db import models


class Ressource(models.Model):
    vhost = models.CharField(max_length=200)

    def __str__(self):
        return self.vhost

    class Meta:
        permissions = (
            ('access_ressource', 'Access ressource'),
        )
