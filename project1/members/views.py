from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def members(request):
    template = loader.get_template('member.html')
    return HttpResponse(template.render())