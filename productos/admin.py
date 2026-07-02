from django.contrib import admin
from .models import Categoria, Inventario, Marca, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activo')
    search_fields = ('nombre',)


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais_origen', 'activo')
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'marca', 'precio', 'stock', 'activo')
    list_filter = ('categoria', 'marca', 'activo')
    search_fields = ('nombre',)


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'tipo_movimiento', 'fecha_movimiento')
    list_filter = ('tipo_movimiento',)
