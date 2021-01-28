from django.shortcuts import render
from .models import Scenario


def index(request):
    latest_scenario_list = Scenario.objects.order_by('-exercise_start')[:5]
    context = {'latest_scenario_list': latest_scenario_list}
    return render(request, 'scenarios/index.html', context)
