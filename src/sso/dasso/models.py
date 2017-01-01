from django.db import models


class Ressource(models.Model):
    vhost = models.CharField(max_length=200)

    def __str__(self):
        return self.vhost

    def matches(self, request):
        return request.split('/')[0] == self.vhost

    @property
    def priority(self):
        return 1

    class Meta:
        permissions = (
            ('access_ressource', 'Access ressource'),
        )
