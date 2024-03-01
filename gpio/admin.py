from django.contrib import admin

from gpio.models import Pins, Board

admin.site.register(Pins)
admin.site.register(Board)
