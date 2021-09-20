
from django.shortcuts import render

def page404(request, exception, template_name='404.html'):
    response = render(request, template_name)
    response.status_code = 404
    print('adas')
    return response