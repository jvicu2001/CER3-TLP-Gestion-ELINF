from django.db import models

class evento(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo_choices = ['Vacaciones', 'Feriado', 'Suspensión de actividades', 'Suspension de actividades pm', 
            'Periodo Lectivo', 'Suspensión de evaluaciones', 'Ceremonia', 'EDDA', 'Evaluacion',
            'Ayudantias', 'Hito académico', 'Secretaria académica', 'OAI']
    tipo = models.CharField(max_length=100, choices=tipo_choices)
    segmento = models.ManyToManyField('segmento')
    def __str__(self):
        return self.titulo
    
class segmento(models.Model):
    nombre = models.CharField(max_length=13)
    def __str__(self):
        return self.nombre


