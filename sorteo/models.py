from django.db import models

class Docentes(models.Model):
    codigo= models.IntegerField()
    ap_paterno = models.CharField(max_length=50)
    ap_materno = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    escuela =   models.CharField(max_length=50)
    condicion = models.CharField(max_length=20)
    sexo = models.CharField(max_length=20)

    class Meta:
        verbose_name = ("Docente")
        verbose_name_plural = ("Docentes")

    def __str__(self):
        return f'{self.codigo} - {self.nombres} {self.ap_paterno} {self.ap_materno}'
class Area(models.Model):

    area = models.CharField( max_length=50)
    cantidad = models.IntegerField()



    class Meta:
        verbose_name = ("Area")
        verbose_name_plural = ("Areas")

    def __str__(self):
        return self.area


class Asignacion(models.Model):
    docente = models.OneToOneField(Docentes, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, related_name='asignaciones', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Asignacion"
        verbose_name_plural = "Asignaciones"

    def __str__(self):
        return f'{self.docente} -> {self.area}'
    




class Administrativos(models.Model):
    codigo= models.IntegerField()
    ap_paterno = models.CharField(max_length=50)
    ap_materno = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    cargo =   models.CharField(max_length=50)
    condicion = models.CharField(max_length=20)
    sexo = models.CharField(max_length=20)

    class Meta:
        verbose_name = ("Administrativos")
        verbose_name_plural = ("Administrativos")

    def __str__(self):
        return f'{self.codigo} - {self.nombres} {self.ap_paterno} {self.ap_materno}'
class Area(models.Model):

    area = models.CharField( max_length=50)
    cantidad = models.IntegerField()


class Invitados(models.Model):
    codigo= models.IntegerField()
    ap_paterno = models.CharField(max_length=50)
    ap_materno = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    cargo =   models.CharField(max_length=50)
    condicion = models.CharField(max_length=20)
    sexo = models.CharField(max_length=20)

    class Meta:
        verbose_name = ("Invitado")
        verbose_name_plural = ("Invitados")

    def __str__(self):
        return f'{self.codigo} - {self.nombres} {self.ap_paterno} {self.ap_materno}'
class Area(models.Model):

    area = models.CharField( max_length=50)
    cantidad = models.IntegerField()
