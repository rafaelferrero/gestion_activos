# Create your views here
from activos.models import Activos, Movimientos
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from decimal import *


@login_required
def getResumenGral(request):
    resumen = []
    registro = []
    plantilla = 'resumen.djhtml'
    activos = Activos.objects.select_related()
    
    for item in activos:
        registro.append(item)
        try:
            movimientos = Movimientos.objects.select_related().filter(
                activo=item.id)
            registro.append(movimientos)
        except ObjectDoesNotExist:
            pass
        resumen.append(registro)
        registro = []
        
    return render_to_response(
        plantilla,
        {'resumen': resumen},
        context_instance=RequestContext(request)
    )


@login_required
def getResumenSeg(request, cmd=''):
    plantilla = 'seguro.djhtml'
    activos = Activos.objects.all().select_related().order_by('codigo')
    stPesos = {}
    stDolar = {}
    tPesos = 0.0
    tDolar = 0.0

    if cmd == 'asegurables':
        activos = Activos.objects.select_related()
        activos = activos.exclude(ubicacion__isnull=True)
        activos = activos.filter(asegurable=True)
        activos = activos.order_by('ubicacion',  'codigo')
    elif cmd == 'asegurados':
        activos = Activos.objects.select_related()
        activos = activos.exclude(ubicacion__isnull=True)
        activos = activos.filter(asegurable=True)
        activos = activos.filter(asegurado=True)
        activos = activos.order_by('codigo')
    elif cmd == 'noasegurados':
        activos = Activos.objects.select_related()
        activos = activos.exclude(ubicacion__isnull=True)
        activos = activos.filter(asegurable=True)
        activos = activos.filter(asegurado=False)
        activos = activos.order_by('codigo')
    elif cmd == 'sinvalorizar':
        activos = Activos.objects.select_related()
        activos = activos.exclude(ubicacion__isnull=True)
        activos = activos.filter(asegurable=True)
        activos = activos.filter(valor=0)
        activos = activos.order_by('codigo')
    elif cmd == 'asegurar':
        activos = Activos.objects.select_related()
        activos = activos.exclude(ubicacion__isnull=True)
        activos = activos.filter(asegurable=True)
        activos = activos.exclude(ubicacion__ubicacion__icontains='ALMACEN')
        activos = activos.order_by('codigo')
        
    for activo in activos:
        if activo.moneda == '$':
            tPesos += float(activo.valor)
            if stPesos.has_key(activo.modelo.tipo):
                stPesos[activo.modelo.tipo] = stPesos.get(activo.modelo.tipo) + float(activo.valor)
            else:
                stPesos[activo.modelo.tipo] = float(activo.valor)
        elif activo.moneda == 'u$s':
            tDolar += float(activo.valor)
            if stDolar.has_key(activo.modelo.tipo):
                stDolar[activo.modelo.tipo] = stDolar.get(activo.modelo.tipo) + float(activo.valor)
            else:
                stDolar[activo.modelo.tipo] = float(activo.valor)
                
    return render_to_response(
        plantilla,
        {
            'activos': activos,
            'stPesos': stPesos,
            'stDolar': stDolar,
            'tPesos': tPesos,
            'tDolar': tDolar,
         },
        context_instance=RequestContext(request)
    )


@login_required
def tmp(request):
    plantilla = 'tmp.djhtml'
    activos = Activos.objects.all().select_related().order_by('codigo').filter(
                    ubicacion__ubicacion='OPTICA')

    return render_to_response(
        plantilla,
        {'activos': activos},
        context_instance=RequestContext(request)
    )
