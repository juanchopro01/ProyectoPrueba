from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Nacionalidad, Equipo, Jugador, PosicionJuego, Tecnico

# Register your models here.

@admin.register(Nacionalidad)
class NacionalidadAdmin(ImportExportModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('nombre',)
    list_per_page = 10
    
class NacionalidadResource(resources.ModelResource):
    class Meta:
        model = Nacionalidad
        fields = ('nombre',)
    
@admin.register(Equipo)
class EquipoAdmin(ImportExportModelAdmin):
    list_display = ('nombre_equipo', 'imagen_bandera', 'escudo_equipo',)
    search_fields = ('nombre_equipo',)
    list_filter = ('nombre_equipo',)
    list_per_page = 10
    
class EquipoResource(resources.ModelResource):
    class Meta:
        model = Equipo
        fields = ('nombre_equipo',)

@admin.register(Jugador)
class JugadorAdmin(ImportExportModelAdmin):
    list_display = ('nombre', 'apellido', 'foto_jugador', 'fecha_nacimiento', 'numero_camiseta', 'equipo' ,'posicion',)
    search_fields = ('nombre', 'apellido', 'fecha_nacimiento', 'numero_camiseta', )
    list_filter = ('nombre', 'apellido', 'fecha_nacimiento', 'numero_camiseta', 'equipo', 'posicion',)
    list_per_page = 10
    
class JugadorResource(resources.ModelResource):
    class Meta:
        model = Jugador
        fields = ('nombre', 'apellido', 'fecha_nacimiento', 'numero_camiseta', 'equipo' ,'posicion',)

@admin.register(PosicionJuego)
class PosicionJuegoAdmin(ImportExportModelAdmin):
    list_display = ('nombre', 'descripcion',)
    search_fields = ('nombre',)
    
class PosicionJuegoResource(resources.ModelResource):
    class Meta:
        model = PosicionJuego
        fields = ('nombre', 'descripcion',)

@admin.register(Tecnico)
class TecnicoAdmin(ImportExportModelAdmin):
    list_display = ('nombre', 'apellido','fecha_nacimiento','nacionalidad', 'rol',)
    search_fields = ('nombre', 'apellido','fecha_nacimiento', 'rol',)
    list_filter = ('nombre', 'apellido','fecha_nacimiento','nacionalidad', 'rol',)
    list_per_page = 10

class TecnicoResource(resources.ModelResource):
    class Meta:
        model = Tecnico
        fields = ('nombre', 'apellido','fecha_nacimiento','nacionalidad', 'rol',)

