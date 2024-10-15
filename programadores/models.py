from django.db import models

# Create your models here.
class Programmer(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('retirado', 'Retirado'),
    ]

    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)

    def __str__(self):
        return f"{self.nombre} ({self.alias})"