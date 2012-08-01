# Create your views here.
from django.shortcuts import redirect
from django.template.context import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie

def home(request):
    return render_to_response('home.html')

@ensure_csrf_cookie
def signing(request):
        return render_to_response('signing.html')


def list_signs(request):
    import os
    signs_files = os.listdir(settings.SINGS_PATH)
    return render_to_response('list_signs.html',{'signs':signs_files})


def save_sign(request):
    if request.POST:
        import re
        datauri = request.POST['canvasData_b64']
        imgstr = re.search(r'base64,(.*)', datauri).group(1)
        import random
        output = open(settings.SINGS_PATH + '/firma-'+str(random.randint(0, 85000000))+'-'+request.POST['nombre_firma']+'.png', 'wb')
        output.write(imgstr.decode('base64'))
        output.close()
    return HttpResponse('{"mensaje":"Guardado OK"}', mimetype='application/json')
