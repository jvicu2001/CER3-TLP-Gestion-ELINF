from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save


class evento(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo_choices = [('V','Vacaciones'), ('F','Feriado'), ('SA','Suspensión de actividades'), ('SAP','Suspension de actividades pm'), 
            ('PL','Periodo Lectivo'), ('SE','Suspensión de evaluaciones'), ('C','Ceremonia'), ('E','EDDA'), ('EV','Evaluacion'),
            ('Ay','Ayudantias'), ('HA','Hito académico'), ('SeA','Secretaria académica'), ('OAI','OAI')]
    tipo = models.CharField(max_length=100, choices=tipo_choices)
    segmento = models.ManyToManyField('segmento')
    def __str__(self):
        return self.titulo
    
class segmento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class UserSegmento(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    segmento = models.ForeignKey(segmento, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username