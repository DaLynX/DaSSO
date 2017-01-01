from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Ressource



def check_user_access(request):
    if ('HTTP_X_ORIGINAL_HOST' in request.META and 'HTTP_X_ORIGINAL_URI' in request.META):
        requested_ressource = request.META['HTTP_X_ORIGINAL_HOST'] + request.META['HTTP_X_ORIGINAL_URI']
    else:
        return HttpResponse(status=500)
    target_ressource = None
    for r in Ressource.objects.all():
        if r.matches(requested_ressource):
            if not target_ressource or target_ressource.priority < r.priority:
                target_ressource = r
    if request.user.has_perm('access_ressource', target_ressource):
        return HttpResponse()
    elif request.user.is_anonymous:
        return HttpResponse(status=401)
    else:
        return HttpResponse(status=403)

def redirect(request, next_url):
    return HttpResponseRedirect('https://' + next_url)
