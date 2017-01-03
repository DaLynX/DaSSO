from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Resource

import logging

logger = logging.getLogger('django.server')

def check_user_access(request):
    if ('HTTP_X_ORIGINAL_HOST' in request.META and 'HTTP_X_ORIGINAL_URI' in request.META):
        requested_resource = request.META['HTTP_X_ORIGINAL_HOST'] + request.META['HTTP_X_ORIGINAL_URI']
        logger.info("Access requested to: [{}]".format(requested_resource))
    else:
        return HttpResponse(status=500)
    target_resource = None
    for r in Resource.objects.all():
        if r.matches(requested_resource):
            if not target_resource or target_resource.priority < r.priority:
                target_resource = r
                logger.info("Selected matching resource: [{}]".format(r))
    if (
            target_resource.public or
            (target_resource.any_authenticated and request.user.is_authenticated()) or
            request.user.has_perm('access_resource', target_resource)
        ):
        logger.info("Access granted to [{}] as per resource [{}].".format(requested_resource, target_resource))
        return HttpResponse()
    elif request.user.is_anonymous:
        return HttpResponse(status=401)
    else:
        return HttpResponse(status=403)

def redirect(request, next_url):
    return HttpResponseRedirect('https://' + next_url)
