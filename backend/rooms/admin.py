from django.contrib import admin
from .models import * # LinkRegularData

admin.site.register(Room)
admin.site.register(RoomLink)
admin.site.register(AuxSilo)
admin.site.register(MainSilo)
#admin.site.register(LinkRegularData)