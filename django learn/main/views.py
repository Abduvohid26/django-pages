from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# def salom(request):
#     return HttpResponse('Assalamu Aleykum')


class HomepageWiev(TemplateView):
    template_name = 'home.html'


class AboutpageWiev(TemplateView):
    template_name = 'about.html'