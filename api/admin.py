from django.contrib import admin
from .models import (
    Especies,
    Arvores,
    GrupoArvores,
    Colheita
    )


admin.site.register(Especies)
admin.site.register(Arvores)
admin.site.register(GrupoArvores)
admin.site.register(Colheita)