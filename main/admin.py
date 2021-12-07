from django.contrib import admin
from .models import *
# Register models here.
admin.site.register(Patient)
admin.site.register(Bed)
admin.site.register(Doctor)