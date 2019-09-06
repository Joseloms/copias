from django.contrib import admin

from .models import Docente
from .models import Nivel
from .models import Copia
# Register your models here.

admin.site.register(Nivel)
admin.site.register(Docente)
admin.site.register(Copia)