from django import forms
from .models import Categoria, Marca, Producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'activo']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError('El nombre es obligatorio.')
        nombre = nombre.strip()
        if not nombre:
            raise forms.ValidationError('El nombre es obligatorio.')
        return nombre


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'pais_origen', 'activo']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError('El nombre es obligatorio.')
        nombre = nombre.strip()
        if not nombre:
            raise forms.ValidationError('El nombre es obligatorio.')
        return nombre


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen', 'categoria', 'marca', 'activo']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError('El nombre es obligatorio.')

        nombre = nombre.strip()
        if not nombre:
            raise forms.ValidationError('El nombre es obligatorio.')

        categoria = self.cleaned_data.get('categoria')
        if categoria:
            queryset = Producto.objects.filter(nombre__iexact=nombre, categoria=categoria)
            if self.instance.pk:
                queryset = queryset.exclude(pk=self.instance.pk)
            if queryset.exists():
                raise forms.ValidationError('Ya existe un producto con este nombre en la misma categoría.')
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor que cero.')
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError('El stock no puede ser menor a cero.')
        return stock

    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria')
        if not categoria:
            raise forms.ValidationError('La categoría es obligatoria.')
        return categoria

    def clean_marca(self):
        marca = self.cleaned_data.get('marca')
        if not marca:
            raise forms.ValidationError('La marca es obligatoria.')
        return marca
