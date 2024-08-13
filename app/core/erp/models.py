from django.db import models
from datetime import datetime


# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Tipo')

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'Tipo'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Categoria')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'Categoria'
        ordering = ['id']

class Empoloyee(models.Model):
    category = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=150, verbose_name='Nombre Completo')
    dni = models.CharField(max_length=10, verbose_name='Identificacion', unique=True)
    date_joined = models.DateField(default=datetime.now(), verbose_name='Fecha de registro')
    date_creation = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'Empleado'
        ordering = ['id']
