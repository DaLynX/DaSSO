from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Ressource


def check_user_access(request, target_vhost):
    target_ressource = Ressource.objects.get(vhost=target_vhost)
    if request.user.has_perm('access_ressource', target_ressource):
        return HttpResponse()
    elif request.user.is_anonymous:
        return HttpResponse(status=401)
    else:
        return HttpResponse(status=403)

def redirect(request, next_url):
    return HttpResponseRedirect('https://' + next_url)
