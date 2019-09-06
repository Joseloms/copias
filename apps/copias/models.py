# encoding:utf-8
from django.db import models


# Create your models here.

class Docente(models.Model):
    name = models.CharField(null=False, max_length=150, verbose_name='Nombre completo')

    def __str__(self):
        return '{}'.format(self.name)


class Nivel(models.Model):
    name = models.CharField(null=False, max_length=150, verbose_name='Descripción')

    def __str__(self):
        return '{}'.format(self.name)


class Copia(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, verbose_name='Docente', null=False)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, verbose_name='Nivel', null=False)
    cantidad = models.IntegerField(null=False)
    detalle = models.CharField(null=True, max_length=300)
    fecha = models.DateField(verbose_name='Fecha', null=True)

    def __str__(self):
        return '{}'.format(self.id)

    def get_string_docente(self):
        return ', '.join([docentes.name for docentes in self.docente.all()])

    def get_string_nivel(self):
        return ', '.join([niveles.name for niveles in self.nivel.all()])
