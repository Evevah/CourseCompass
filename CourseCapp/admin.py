from django.contrib import admin
from .models import Feature
from .models import Section1
from .models import Section2
from .models import Section3
from .models import Section4
from .models import results
from .models import Room
from .models import Message
from .models import COMUD

admin.site.register(Feature)
admin.site.register(Section1)
admin.site.register(results)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Section2)
admin.site.register(Section3)
admin.site.register(Section4)
admin.site.register(COMUD)
# Register your models here.
