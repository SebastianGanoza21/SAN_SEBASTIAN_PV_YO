from django import forms
from .models import Producto,Proveedor

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo_producto', 'codigo_barras', 'nombre', 'precio', 'stock', 'imagen', 'categoria', 'marca', 'proveedor']
        widgets = {
            'codigo_producto': forms.TextInput(attrs={'placeholder': 'Introduce el código de producto'}),
            'codigo_barras': forms.TextInput(attrs={'placeholder': 'Introduce el código de barras'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Introduce el nombre del producto'}),
            'precio': forms.NumberInput(attrs={'placeholder': 'Introduce el precio (USD)'}),
            'stock': forms.NumberInput(attrs={'placeholder': 'Introduce el stock'}),
            'categoria': forms.Select(attrs={'placeholder': 'Selecciona la categoría'}),
            'marca': forms.Select(attrs={'placeholder': 'Selecciona la marca'}),
            'proveedor': forms.Select(attrs={'placeholder': 'Selecciona el proveedor'}),
            'imagen': forms.ClearableFileInput(attrs={'placeholder': 'Selecciona una imagen'}),
        }


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['codigo_proveedor', 'nombres', 'apellidos', 'ruc_dni', 'direccion', 'correo_electronico', 'numero_telefono']
        labels = {
            'codigo_proveedor': 'Código de Proveedor',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'ruc_dni': 'RUC/DNI',
            'direccion': 'Dirección',
            'correo_electronico': 'Correo Electrónico',
            'numero_telefono': 'Número de Teléfono',
        }
        widgets = {
            'codigo_proveedor': forms.TextInput(attrs={'placeholder': 'Código de Proveedor'}),
            'nombres': forms.TextInput(attrs={'placeholder': 'Nombres'}),
            'apellidos': forms.TextInput(attrs={'placeholder': 'Apellidos'}),
            'ruc_dni': forms.TextInput(attrs={'placeholder': 'RUC/DNI'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Dirección'}),
            'correo_electronico': forms.EmailInput(attrs={'placeholder': 'Correo Electrónico'}),
            'numero_telefono': forms.TextInput(attrs={'placeholder': 'Número de Teléfono'}),
        }