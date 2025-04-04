from django.contrib import admin
from .models import Medico
from .models import Consulta

# Register your models here.
admin.site.register(Medico)
admin.site.register(Consulta)