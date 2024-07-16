from django import forms
from .models import Edificio, Departamento

class EdificioForm(forms.ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']

    def clean_ciudad(self):
        ciudad = self.cleaned_data['ciudad']
        if ciudad.startswith('L'):
            raise forms.ValidationError("El nombre de la ciudad no puede iniciar con la letra mayúscula L")
        return ciudad
    
#DEPARTAMENTOS

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_propietario', 'costo', 'numero_cuartos', 'edificio']

    def clean_nombre_propietario(self):
        nombre = self.cleaned_data['nombre_propietario']
        if len(nombre.split()) < 3:
            raise forms.ValidationError("El nombre completo del propietario debe tener al menos 3 palabras")
        return nombre
    
    def clean_costo(self):
        costo = self.cleaned_data['costo']
        if (costo) > 100000:
            raise forms.ValidationError("El costo no puede ser mayor a $100 mil")
        return costo
    
    def clean_costo(self):
        numero_cuartos = self.cleaned_data['numero_cuartos']
        if (numero_cuartos == 0 and numero_cuartos > 7):
            raise forms.ValidationError("El departamento no puede mas de 7 cuartos ni 0")
        return numero_cuartos