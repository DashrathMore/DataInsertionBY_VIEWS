from django.contrib import admin

# Register your models here.

from app.models import *

admin.site.register(Liabrary)

admin.site.register(Books)

admin.site.register(reader)

admin.site.register(reading)