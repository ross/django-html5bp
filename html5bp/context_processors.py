#
#
#

from __future__ import absolute_import

from django.conf import settings

def html5bp(request):
    return getattr(settings, 'HTML5BP', {})
