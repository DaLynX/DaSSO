from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Ressource

import logging

logger = logging.getLogger('django.server')

def check_user_access(request):
    if ('HTTP_X_ORIGINAL_HOST' in request.META and 'HTTP_X_ORIGINAL_URI' in request.META):
        requested_ressource = request.META['HTTP_X_ORIGINAL_HOST'] + request.META['HTTP_X_ORIGINAL_URI']
        logger.info("Access requested to: [{}]".format(requested_ressource))
    else:
        return HttpResponse(status=500)
    target_ressource = None
    for r in Ressource.objects.all():
        if r.matches(requested_ressource):
            if not target_ressource or target_ressource.priority < r.priority:
                target_ressource = r
                logger.info("Selected matching ressource: [{}]".format(r))
    if (
            target_ressource.public or
            (target_ressource.any_authenticated and request.user.is_authenticated()) or
            request.user.has_perm('access_ressource', target_ressource)
        ):
        logger.info("Access granted to [{}] as per ressource [{}].".format(requested_ressource, target_ressource))
        return HttpResponse()
    elif request.user.is_anonymous:
        return HttpResponse(status=401)
    else:
        return HttpResponse(status=403)

def redirect(request, next_url):
    return HttpResponseRedirect('https://' + next_url)
