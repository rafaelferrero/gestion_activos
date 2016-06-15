from django.contrib import admin
from activos.models import Marcas
from activos.models import Modelos
from activos.models import Activos
from activos.models import Estados
from activos.models import Movimientos
from activos.models import Ubicaciones
from activos.models import Incidencias
from activos.models import Tipos


class MarcasAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca')
    list_filter = ('marca',)
    search_fields = ('marca',)


class ModelosAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo','marca','modelo')
    list_filter = ('tipo','marca')
    search_fields = ('modelo','marca__marca','tipo__tipo')


class ActivosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 
                    'moneda', 
                    'valor', 
                    'asegurable', 
                    'asegurado', 
                    'ubicacion', 
                    'numero_serie', 
                    'modelo', 
                    'detalle')
    list_filter = ('asegurable','asegurado','ubicacion','modelo__tipo__tipo')
    search_fields = ('codigo', 'numero_serie', 'nro_factura', 'detalle', 'ubicacion__ubicacion', 
                     'modelo__modelo', 'modelo__marca__marca', 'modelo__tipo__tipo')
    actions = ['asegurar','no_asegurar','hacer_asegurable','hacer_no_asegurable']

    def asegurar(self, request, queryset):
        queryset.update(asegurado=True)
    asegurar.short_description = "Marcar estos Activos como Asegurados"

    def no_asegurar(self, request, queryset):
        queryset.update(asegurado=False)
    no_asegurar.short_description = "Marcar estos Activos como NO Asegurados"

    def hacer_asegurable(self, request, queryset):
        queryset.update(asegurable=True)
    hacer_asegurable.short_description = "Marcar estos Activos como Asegurables"
    
    def hacer_no_asegurable(self, request, queryset):
        queryset.update(asegurable=False)
    hacer_no_asegurable.short_description = "Marcar estos Activos como NO Asegurables"
    

class EstadosAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado')
    list_filter=('estado',)
    search_fields=('estado',)


class MovimientosAdmin(admin.ModelAdmin):
    list_display = ('id','fecha','activo', 'origen','destino')
    list_filter=('fecha','origen','destino','activo')
    date_hierarchy='fecha'
    search_fields=('fecha','origen__ubicacion','destino__ubicacion',
                   'activo__codigo','activo__numero_serie','activo__modelo__modelo',
                   'activo__modelo__marca__marca','activo__modelo__tipo__tipo')

class UbicacionesAdmin(admin.ModelAdmin):
    list_display = ('ubicacion',)
    list_filter=('ubicacion',)
    search_fields=('ubicacion',)


class IncidenciasAdmin(admin.ModelAdmin):
    list_display = ('id','fecha', 'activo','estado','descripcion')
    list_filter=('fecha','activo','estado')
    date_hierarchy= 'fecha'
    search_fields=('fecha','descripcion','activo__codigo','activo__numero_serie',
                   'activo__modelo__modelo','activo__modelo__marca__marca','activo__modelo__tipo__tipo',
                   'estado__estado')


class TiposAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')
    list_filter=('tipo',)
    search_fields=('tipo',)
    

admin.site.register(Marcas, MarcasAdmin)
admin.site.register(Modelos, ModelosAdmin)
admin.site.register(Activos, ActivosAdmin)
admin.site.register(Estados, EstadosAdmin)
admin.site.register(Movimientos, MovimientosAdmin)
admin.site.register(Ubicaciones, UbicacionesAdmin)
admin.site.register(Incidencias, IncidenciasAdmin)
admin.site.register(Tipos, TiposAdmin)
