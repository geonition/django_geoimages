from django.http import HttpResponse
from django.utils import simplejson as json

def geoimage(request):

    image_parameters = {
        'name': 'testimage',
        'url': '',
        'extent': {
            'left': 0,
            'rigth': 0
        }
    }

    return HttpResponse(json.dumps(image_parameters),
                        content_type="json/application")
