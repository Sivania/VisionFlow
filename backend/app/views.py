from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from .models import Action
import json

@require_http_methods(["GET", "POST"])
def action(request):
    if request.method == "GET":
        flows = list(Action.objects.values())
        return JsonResponse(flows, safe=False)
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            flow = Action.objects.create(**data)
            return JsonResponse({"id": flow.id, "name": flow.name, "description": flow.description}, status=201)
        except (ValueError, KeyError):
            return HttpResponseBadRequest("Invalid data provided.")