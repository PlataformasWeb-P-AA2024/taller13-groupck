from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Edificio(models.Model):
    TIPOS = [
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
    ]
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS)

    def __str__(self):
        return self.nombre

    def total_cuartos(self):
        return sum(depto.numero_cuartos for depto in self.departamentos.all())

    def costo_total_departamentos(self):
        return sum(depto.costo for depto in self.departamentos.all())

class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=200)
    costo = models.DecimalField(max_digits=10, decimal_places=2, validators=[MaxValueValidator(100000)])
    numero_cuartos = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)])
    edificio = models.ForeignKey(Edificio, related_name='departamentos', on_delete=models.CASCADE)

    def __str__(self):
        return f"Departamento de {self.nombre_propietario}"