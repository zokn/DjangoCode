from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.
#BUSQUEDA
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "tfno")
    search_fields=("nombre", "tfno")

#FILTROS 
class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

##class PedidosAdmin(admin.ModelAdmin):
    #agregar un display para mejorar la visualizacion
    ##list_display("nombre", "fecha")
    #list_filter=("fecha",)

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos)