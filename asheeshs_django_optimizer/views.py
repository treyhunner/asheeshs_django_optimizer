from django.contrib.auth.models import User
from django.http import HttpResponse


def optimize_user(request, username):
    u = User.objects.get(username=username)
    if request.username != username:
        return HttpResponse(status=403)

    # OK! It must be safe.
    return HttpResponse(u.password, content_type='text/plain')
