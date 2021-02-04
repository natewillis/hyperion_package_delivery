from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import datetime

# Create your models here.
# default values
DEFAULT_COUNTRY_ID = 1
DEFAULT_WAVE = 1
DEFAULT_POINT = Point(0, 0, srid=4326)
DEFAULT_PAGE_DISPLAY_NAME = 'FORD TRANSIT VAN'
DEFAULT_DELIVERY_TYPE = 'FTV'
DEFAULT_MESSAGE_COUNTRY_CODE = 'XXX'
DEFAULT_SCENARIO = 1


class Scenario(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    exercise_start = models.DateTimeField(default=datetime.datetime.now)
    scenario_start = models.DateTimeField(default=datetime.datetime.now)


class Shipment(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, default=DEFAULT_COUNTRY_ID)
    country = models.ForeignKey('world.WorldBorder', on_delete=models.CASCADE, default=DEFAULT_COUNTRY_ID)
    wave = models.CharField(max_length=2, default=DEFAULT_WAVE)
    start_location = models.PointField(default=DEFAULT_POINT)
    start_datetime = models.DateTimeField(default=datetime.datetime.now)
    page_display_name = models.CharField(max_length=200, default=DEFAULT_PAGE_DISPLAY_NAME)
    message_delivery_type = models.CharField(max_length=200, default=DEFAULT_DELIVERY_TYPE)
    message_country_code = models.CharField(max_length=10, default=DEFAULT_MESSAGE_COUNTRY_CODE)


class Delivery(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='deliveries')
    package_weight = models.FloatField(default=0)
    end_location = models.PointField(default=DEFAULT_POINT)
    end_datetime = models.DateTimeField(default=datetime.datetime.now)
    message_country_code = models.CharField(max_length=10, default=DEFAULT_MESSAGE_COUNTRY_CODE)
    placement = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'Deliveries'
