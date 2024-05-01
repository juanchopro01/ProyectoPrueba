from django.db import models

class Nacionalidad(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        verbose_name = "NATIONALITY"
        verbose_name_plural = "Nacionalidades"
        db_table = "Nacionalidades"
        ordering = ['nombre']
        
    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=255)
    imagen_bandera = models.ImageField(upload_to='banderas/')
    escudo_equipo = models.ImageField(upload_to='escudos/')

    class Meta:
        verbose_name = "team"
        verbose_name_plural = "Equipos"
        db_table = "Equipo"
        ordering = ['nombre_equipo']

    def __str__(self):
        return self.nombre_equipo

class PosicionJuego(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    class Meta:
        verbose_name = "position"
        verbose_name_plural = "Posiciones"
        db_table = "Posicion"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    foto_jugador = models.ImageField(upload_to='fotos_jugadores/')
    fecha_nacimiento = models.DateField()
    numero_camiseta = models.IntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    posicion = models.ForeignKey(PosicionJuego, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "player"
        verbose_name_plural = "Jugadores"
        db_table = "jugador"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Tecnico(models.Model):
    ROL_CHOICES = [
        ('Técnico', 'Técnico'),
        ('Asistente', 'Asistente'),
        ('Médico', 'Médico'),
        ('Preparador', 'Preparador'),
    ]

    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    rol = models.CharField(max_length=255, choices=ROL_CHOICES)
    
    class Meta:
        verbose_name = "coach"
        verbose_name_plural = "Técnicos"
        db_table = "Tecnico"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


