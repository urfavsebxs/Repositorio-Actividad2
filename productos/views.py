from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import CategoriaForm, MarcaForm, ProductoForm
from .models import Categoria, Marca, Producto


def listar_productos(request):
    productos = Producto.objects.select_related('categoria', 'marca').order_by('-fecha_creacion')
    paginator = Paginator(productos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'productos/lista.html', {'page_obj': page_obj})


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto registrado correctamente.')
            return redirect('listar_productos')
    else:
        form = ProductoForm()

    categorias = Categoria.objects.filter(activo=True).order_by('nombre')
    marcas = Marca.objects.filter(activo=True).order_by('nombre')
    return render(request, 'productos/crear.html', {'form': form, 'categorias': categorias, 'marcas': marcas})


def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría registrada correctamente.')
            return redirect('crear_producto')
    else:
        form = CategoriaForm()

    return render(request, 'productos/crear_categoria.html', {'form': form})


def crear_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marca registrada correctamente.')
            return redirect('crear_producto')
    else:
        form = MarcaForm()

    return render(request, 'productos/crear_marca.html', {'form': form})


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente.')
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)

    categorias = Categoria.objects.filter(activo=True).order_by('nombre')
    marcas = Marca.objects.filter(activo=True).order_by('nombre')
    return render(request, 'productos/editar.html', {'form': form, 'producto': producto, 'categorias': categorias, 'marcas': marcas})


def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('listar_productos')

    return render(request, 'productos/eliminar.html', {'producto': producto})
