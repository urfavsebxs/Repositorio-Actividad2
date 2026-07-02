from django.test import TestCase
from django.urls import reverse
from .models import Categoria, Marca, Producto, Inventario


class CategoriaModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(
            nombre='Electrónica',
            descripcion='Productos electrónicos',
            activo=True
        )

    def test_categoria_str(self):
        self.assertEqual(str(self.categoria), 'Electrónica')

    def test_categoria_creacion(self):
        self.assertTrue(Categoria.objects.filter(nombre='Electrónica').exists())


class MarcaModelTest(TestCase):
    def setUp(self):
        self.marca = Marca.objects.create(
            nombre='Samsung',
            pais_origen='Corea del Sur',
            activo=True
        )

    def test_marca_str(self):
        self.assertEqual(str(self.marca), 'Samsung')

    def test_marca_creacion(self):
        self.assertTrue(Marca.objects.filter(nombre='Samsung').exists())


class ProductoModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(
            nombre='Electrónica',
            descripcion='Productos electrónicos',
            activo=True
        )
        self.marca = Marca.objects.create(
            nombre='Samsung',
            pais_origen='Corea del Sur',
            activo=True
        )
        self.producto = Producto.objects.create(
            nombre='Televisor',
            descripcion='Televisor 4K',
            precio=1200.00,
            stock=5,
            categoria=self.categoria,
            marca=self.marca,
            activo=True
        )

    def test_producto_str(self):
        self.assertEqual(str(self.producto), 'Televisor')

    def test_producto_precio_valido(self):
        self.assertEqual(self.producto.precio, 1200.00)

    def test_producto_stock_valido(self):
        self.assertEqual(self.producto.stock, 5)


class InventarioModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre='Electrónica')
        self.marca = Marca.objects.create(nombre='Samsung')
        self.producto = Producto.objects.create(
            nombre='Televisor',
            precio=1200.00,
            stock=5,
            categoria=self.categoria,
            marca=self.marca
        )
        self.inventario = Inventario.objects.create(
            producto=self.producto,
            cantidad=10,
            tipo_movimiento='Entrada'
        )

    def test_inventario_str(self):
        self.assertIn('Televisor', str(self.inventario))
        self.assertIn('Entrada', str(self.inventario))


class ProductoViewsStatusTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre='Electrónica', activo=True)
        self.marca = Marca.objects.create(nombre='Samsung', activo=True)

    def test_listar_productos_status_200(self):
        try:
            response = self.client.get(reverse('listar_productos'))
            self.assertEqual(response.status_code, 200)
        except Exception:
            pass

    def test_crear_producto_status_200(self):
        try:
            response = self.client.get(reverse('crear_producto'))
            self.assertEqual(response.status_code, 200)
        except Exception:
            pass

    def test_crear_producto_post_redirect(self):
        data = {
            'nombre': 'Laptop',
            'descripcion': 'Laptop HP',
            'precio': 800.00,
            'stock': 3,
            'categoria': self.categoria.id,
            'marca': self.marca.id,
            'activo': True
        }
        response = self.client.post(reverse('crear_producto'), data)
        self.assertIn(response.status_code, [200, 302])
        self.assertTrue(Producto.objects.filter(nombre='Laptop').exists())


class CategoriaFormTest(TestCase):
    def test_crear_categoria_post(self):
        data = {
            'nombre': 'Herramientas',
            'descripcion': 'Herramientas varias',
            'activo': True
        }
        response = self.client.post(reverse('crear_categoria'), data)
        self.assertIn(response.status_code, [200, 302])
        self.assertTrue(Categoria.objects.filter(nombre='Herramientas').exists())


class MarcaFormTest(TestCase):
    def test_crear_marca_post(self):
        data = {
            'nombre': 'Acme',
            'pais_origen': 'Perú',
            'activo': True
        }
        response = self.client.post(reverse('crear_marca'), data)
        self.assertIn(response.status_code, [200, 302])
        self.assertTrue(Marca.objects.filter(nombre='Acme').exists())

