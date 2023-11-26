from django.db import models

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
    nombre = models.CharField(max_length=13)
    def __str__(self):
        return self.nombre


