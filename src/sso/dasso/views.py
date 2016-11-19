from django.shortcuts import render
from django.http import HttpResponse

from .models import Ressource


def check_user_access(request, target_vhost):
    target_ressource = Ressource.objects.get(vhost=target_vhost)
    if request.user.has_perm('access_ressource', target_ressource):
        return HttpResponse()
    else:
        return HttpResponse(status=403)
