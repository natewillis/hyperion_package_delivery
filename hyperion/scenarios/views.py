from django.shortcuts import render
from .models import Scenario, Delivery, Shipment


def index(request):
    latest_scenario_list = Scenario.objects.order_by('-exercise_start')[:5]
    context = {'latest_scenario_list': latest_scenario_list}
    return render(request, 'scenarios/index.html', context)


def raw_messages(request, scenario_id):
    shipments = Shipment.objects.filter(scenario_id=scenario_id).order_by('start_datetime')
    deliveries = Delivery.objects.filter(shipment__scenario_id=scenario_id)

    # init message dict
    messages = {}

    # shipment logic
    for shipment in shipments:

        # format the message key
        message_key_int = 1
        message_key = f'{shipment.start_datetime.strftime("%Y%m%d%H%M%S")}_{message_key_int:05d}'
        while message_key in messages:
            message_key_int += 1
            message_key = f'{shipment.start_datetime.strftime("%Y%m%d%H%M%S")}_{message_key_int:05d}'

        # create the message
        message = f'{message_key} shipment from {shipment.country.name}'

        # store the message
        messages[message_key] = message

    # delivery logic
    for delivery in deliveries:

        # format the message key
        message_key_int = 1
        message_key = f'{delivery.end_datetime.strftime("%Y%m%d%H%M%S")}_{message_key_int:05d}'
        while message_key in messages:
            message_key_int += 1
            message_key = f'{delivery.end_datetime.strftime("%Y%m%d%H%M%S")}_{message_key_int:05d}'

        # create the message
        message = f'{message_key} delivery with a weight of {delivery.package_weight} lbs'

        # store the message
        messages[message_key] = message

    context = {'messages': [messages[message_key] for message_key in sorted(messages.keys())]}
    return render(request, 'scenarios/raw_messages.html', context)


