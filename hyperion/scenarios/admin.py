from django.contrib import admin
from .models import Scenario, Shipment, Delivery

# Register your models here.
admin.site.register(Scenario)
admin.site.register(Shipment)
admin.site.register(Delivery)
