from django.contrib import admin
from .models import homeModel
from .models import Message
from .models import ownerModel
from .models import roomModel
from .models import openPatternModel
from .models import roomGroupModel
from .models import timeTableModel
from .models import illegalDayModel
from .models import reservationModel

admin.site.register(homeModel)
admin.site.register(Message)
admin.site.register(ownerModel)
admin.site.register(roomModel)
admin.site.register(openPatternModel)
admin.site.register(roomGroupModel)
admin.site.register(timeTableModel)
admin.site.register(illegalDayModel)
admin.site.register(reservationModel)
