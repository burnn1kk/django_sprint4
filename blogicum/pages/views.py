from django.shortcuts import render
from django.views.generic import TemplateView


def about(request):
    template_name = 'pages/about.html'
    return render(request, template_name)


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class RulesPageView(TemplateView):
    template_name = 'pages/rules.html'


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def error_500(request):
    return render(request, 'pages/500.html', status=500)
