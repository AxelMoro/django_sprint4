from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

def about(request):
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    template = 'pages/rules.html'
    return render(request, template)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def handler500(request, exception):
    return render(request, 'pages/405.html', status=405)
