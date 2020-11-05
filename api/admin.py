import csv, decimal

from django.contrib import admin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from nested_inline.admin import NestedStackedInline, NestedModelAdmin


from .models import (
    Especies,
    Arvores,
    GrupoArvores,
    Colheita
    )


def export_colheita(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="colheita.csv"'
    writer = csv.writer(response)
    writer.writerow(['Árvores', 'Data da colheita', 'Grupo das Árvores', 'Espécies'])
    colheitas = queryset.values_list('arvore__descricao', 'data_colheita', 'grupo_arvores__nome', 'especies__descricao')
    for c in colheitas:
        writer.writerow(c)
    return response
export_colheita.short_description = 'Exportar para CSV'


class EspeciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    search_fields = ('id', 'descricao')


class ArvoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'especies', 'descricao', 'idade')
    search_fields = ('id', 'especies__descricao', 'descricao', 'idade')


class GrupoArvoresAdmin(admin.ModelAdmin):
    fields = ['nome', 'descricao', 'arvores']
    list_display = ('id', 'nome','descricao',)
    search_fields = ('id', 'nome', 'descricao')


class ColheitaAdmin(admin.ModelAdmin):
    readonly_fields = ['especies']
    list_display = ('informacoes', 'data_colheita', 'peso_bruto', 'arvore', 'grupo_arvores', 'especies')
    search_fields = ('informacoes','arvore__descricao', 'grupo_arvores__nome', 'especies__descricao')
    actions = [export_colheita,]



admin.site.register(Especies, EspeciesAdmin)
admin.site.register(Arvores, ArvoresAdmin)
admin.site.register(GrupoArvores, GrupoArvoresAdmin)
admin.site.register(Colheita, ColheitaAdmin)
