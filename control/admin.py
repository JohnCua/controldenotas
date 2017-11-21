from django.contrib import admin

# Register your models here.
from control.models import Materia, MateriaAdmin, Grado, GradoAdmin
# Register your models here.
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Grado, GradoAdmin)
