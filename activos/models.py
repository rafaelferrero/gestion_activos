from django.db import models
from datetime import datetime
    

class Marcas(models.Model):
    marca = models.CharField(
        max_length=200)
    
    def __unicode__(self):
        return self.marca
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['marca']


class Tipos(models.Model):
    tipo = models.CharField(
        max_length=200)
    
    def __unicode__(self):
        return self.tipo
    
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['tipo']


class Modelos(models.Model):
    modelo = models.CharField(
        max_length=200)
    marca = models.ForeignKey(
        Marcas)
    tipo = models.ForeignKey(
        Tipos)
    
    def __unicode__(self):
        return u"{0} - {1} - {2}".format(
            self.tipo,
            self.marca,
            self.modelo)

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'
        ordering = ['tipo', 'marca', 'modelo']


class Ubicaciones(models.Model):
    ubicacion = models.CharField(
        max_length=200)
    
    def __unicode__(self):
        return self.ubicacion

    class Meta:
        verbose_name = 'Ubicacion'
        verbose_name_plural = 'Ubicaciones'
        ordering = [ 'ubicacion' ]


class Activos(models.Model):
    PESOS = '$'
    DOLLAR = 'u$s'
    MONEDA_CHOICES = (
        (PESOS, '$'),
        (DOLLAR, 'u$s'),
    )

    codigo = models.CharField(
        'Codigo Interno',
        max_length=7,
        unique=True)
    numero_serie = models.CharField(
        max_length=200)
    modelo = models.ForeignKey(Modelos)
    nro_factura = models.CharField(
        max_length=50,
        blank=True,
        null=True)
    moneda = models.CharField(
        max_length=3,
        choices=MONEDA_CHOICES,
        default=PESOS)
    valor = models.DecimalField(
        'Valor Declarado',
        max_digits=11,
        decimal_places=2,
        blank=True,
        null=True)
    detalle = models.CharField(
        max_length=500,
        blank=True)
    ubicacion = models.ForeignKey(
        Ubicaciones,
        blank=True,
        null=True)
    asegurable = models.BooleanField(
        default=False)
    asegurado = models.BooleanField(
        default=False)

    def __unicode__(self):
        return u"{0} - {1} - {2} - {3}".format(
            self.codigo,
            self.modelo,
            self.numero_serie,
            self.ubicacion)

    class Meta:
        verbose_name = 'Activo'
        verbose_name_plural = 'Activos'
        ordering = [ 'codigo', 'ubicacion']


class Movimientos(models.Model):
    activo = models.ForeignKey(
        Activos)
    origen = models.ForeignKey(
        Ubicaciones,
        related_name='ubicacion_origen')
    destino = models.ForeignKey(
        Ubicaciones,
        related_name='ubicacion_destino')
    fecha = models.DateTimeField(
        default=datetime.now())
    
    def __unicode__( self ):
        return u"{0}: de {1} a {2}".format(
            self.activo,
            self.origen,
            self.destino)

    def save(self, *args, **kwargs):
        a = Activos.objects.get(pk=self.activo.pk)
        a.ubicacion = self.destino
        a.save(update_fields=['ubicacion'])
        super(Movimientos, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Movimiento del Activo'
        verbose_name_plural = 'Movimientos de los Activos'
        ordering = [ '-fecha', 'activo']


class Estados(models.Model):
    estado=models.CharField(
        max_length=200)
    
    def __unicode__(self):
        return self.estado

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['estado']

    
class Incidencias(models.Model):
    activo = models.ForeignKey(
        Activos)
    estado = models.ForeignKey(
        Estados)
    fecha = models.DateTimeField(
        default=datetime.now())
    descripcion = models.TextField()
    
    def __unicode__(self):
        return u"{0} ({1}): {2}".format(
            self.activo,
            self.estado,
            self.descripcion)
    
    class Meta:
        verbose_name = 'Incidencia del Activo'
        verbose_name_plural = 'Incidencias de los Activos'
        ordering = ['-fecha', 'activo', 'estado']

