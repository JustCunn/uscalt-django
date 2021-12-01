from background_task import background
from .models import Room, RoomLink, MainSilo, AuxSilo 
from .serializers import RoomInfoSerializer, RoomLinkSerializer, RegisterRoom, MainSiloSerializer, AuxSiloSerializer

from datetime import datetime, date

@background(schedule=10)
def check_and_delete():
    links = RoomLink.objects.all()
    
    for link in links:
        u_time = datetime.now()
        if (link.call_time - u_time).seconds > 7200:
            AuxSilo.objects.filter(link=link.display_name).delete()
            