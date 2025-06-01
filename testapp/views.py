import json

from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import render

import testapp.models
from testapp.models import Clicks


def index_page(request):
    try:
        clicks = Clicks.objects.latest("timestamp")
        context = {"amount": clicks.count}
    except testapp.models.Clicks.DoesNotExist:
        context = {"amount": 0}

    return render(request, "index.html", context)


def set_clicks(request):
    if request.method == "POST":
        clicks = int(request.body.decode())
        obj = Clicks(count=clicks)
        obj.save()
        return JsonResponse([clicks], safe=False)
    elif request.method == "GET":
        return HttpResponseNotFound

