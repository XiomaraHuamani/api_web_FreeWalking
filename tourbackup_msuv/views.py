from django.shortcuts import render
from django.http import HttpResponse
from .serializers import RegionSerializer
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from .models import *

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

##from django.http import JSONResponse
from rest_framework.renderers import JSONRenderer

from django.shortcuts import render,redirect
# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs["content_type"] = "application/json"
        super(JSONResponse, self).__init__(content, **kwargs)


def harrys(request):
    return HttpResponse("harrysito es el mas pulento")


def juan(request):
    return HttpResponse("pagueme al final de la clase")


# @csrf_exempt
#  def rf_region(request):
#    if request.method == "GET":
#     return HttpResponse("restfull GET List")
#    elif request.method == "POST":
#     return HttpResponse("restfull POST")
#ejemplo 1 
@csrf_exempt
def harrysSerializer(request):
    choice = choice.objects.all()
    serializer = HarrysSerializer(choice, many=True)
    # return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    return JSONResponse(serializer.data)


#######LLAMADO DE TABLA REGION#########
#######LLAMADO DE TABLA REGION#########
#######LLAMADO DE TABLA REGION#########


@csrf_exempt ##metodo de llamado general
def rf_region(request):
    if request.method == "GET":
        region =  Region.objects.all()
        serializer = RegionSerializer(region,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        region = RegionSerializer(data=data)
        if region.is_valid():
            region.save()
            return JSONResponse(region.data, status=201)
    return JSONResponse(region.errors, status=400)

@csrf_exempt ##metodo de llamado especifico
def rf_region_reg(request, cod_region):
    try:
        region = Region.objects.get(pk=cod_region)
    except region.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
          #ya lo ley antes en el try
         region= RegionSerializer(region)
         return JSONResponse(region.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        region = RegionSerializer(data=data)
        print(data)
        if region.is_valid():
            region.save()
            return JSONResponse(region.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        region_serializer = RegionSerializer(region, data=data, partial=True)
        if region_serializer.is_valid():
            region_serializer.save()
            return JSONResponse(region_serializer.data)              
    elif request.method == "DELETE":
            #ya lo ley antes en el try
            region.delete()
            return HttpResponse(status=400)
    return JSONResponse(region.errors, status=400)


#######LLAMADO DE TABLA CONTACTO#########
#######LLAMADO DE TABLA CONTACTO#########
#######LLAMADO DE TABLA CONTACTO#########


@csrf_exempt ##metodo de llamado general
def rf_contacto(request):
    if request.method == "GET":
        contacto =  Contacto.objects.all()
        serializer = ContactoSerializer(contacto,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        contacto = ContactoSerializer(data=data)
        if contacto.is_valid():
            contacto.save()
            return JSONResponse(contacto.data, status=201)
    return JSONResponse(contacto.errors, status=300)

@csrf_exempt ##metodo de llamado especifico
def rf_contacto_reg(request, id_contacto):
    try:
        contacto = Contacto.objects.get(pk=id_contacto)
    except contacto.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
          #ya lo ley antes en el try
         contacto= ContactoSerializer(contacto)
         return JSONResponse(contacto.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        contacto = ContactoSerializer(data=data)
        print(data)
        if contacto.is_valid():
            contacto.save()
            return JSONResponse(contacto.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        contacto_serializer = ContactoSerializer(contacto, data=data, partial=True)
        if contacto_serializer.is_valid():
            contacto_serializer.save()
            return JSONResponse(contacto_serializer.data)              
    elif request.method == "DELETE":
            #ya lo ley antes en el try
            contacto.delete()
            return HttpResponse(status=400)
    return JSONResponse(contacto.errors, status=400)


#######LLAMADO DE TABLA CALIDAD TOUR#########
#######LLAMADO DE TABLA CALIDAD TOUR#########
#######LLAMADO DE TABLA CALIDAD TOUR#########


@csrf_exempt ###metodo de llamado general
def rf_calidadtour(request):
    if request.method == "GET":
        calidadtour =  CalidadTour.objects.all()
        serializer = CalidadTourSerializer(calidadtour,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        calidadtour = CalidadTourSerializer(data=data)
        if calidadtour.is_valid():
            calidadtour.save()
            return JSONResponse(calidadtour.data, status=201)
    return JSONResponse(calidadtour.errors, status=400)


@csrf_exempt ##metodo de llamado especifico
def rf_calidadtour_reg(request, cod_region):
    try:
        calidadtour = CalidadTour.objects.get(pk=cod_region)
    except calidadtour.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
          #ya lo ley antes en el try
         calidadtour= CalidadTourSerializer(calidadtour)
         return JSONResponse(calidadtour.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        calidadtour = CalidadTourSerializer(data=data)
        print(data)
        if calidadtour.is_valid():
            calidadtour.save()
            return JSONResponse(calidadtour.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        calidadtour_serializer = CalidadTourSerializer(calidadtour, data=data, partial=True)
        if calidadtour_serializer.is_valid():
            calidadtour_serializer.save()
            return JSONResponse(calidadtour_serializer.data)              
    elif request.method == "DELETE":
            #ya lo ley antes en el try
            calidadtour.delete()
            return HttpResponse(status=400)
    return JSONResponse(calidadtour.errors, status=400)
    
#######LLAMADO DE TABLA  evaluacion#########
#######LLAMADO DE TABLA  evaluacion#########
#######LLAMADO DE TABLA  evaluacion#########

@csrf_exempt ###metodo de llamado general
def rf_categoriaeva(request):
    if request.method == "GET":
        categoriaeva =  CategoriaEva.objects.all()
        serializer = CategoriaEvaSerializer(categoriaeva,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        categoriaeva = CategoriaEvaSerializer(data=data)
        if categoriaeva.is_valid():
            categoriaeva.save()
            return JSONResponse(categoriaeva.data, status=201)
    return JSONResponse(categoriaeva.errors, status=400)



@csrf_exempt ##metodo de llamado especifico
def rf_categoriaeva_reg(request, id_cat_eva):
    try:
        categoriaeva = CategoriaEva.objects.get(pk=id_cat_eva)
    except categoriaeva.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
          #ya lo ley antes en el try
         categoriaeva= CategoriaEvaSerializer(categoriaeva)
         return JSONResponse(categoriaeva.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        categoriaeva = CategoriaEvaSerializer(data=data)
        if categoriaeva.is_valid():
            categoriaeva.save()
            return JSONResponse(categoriaeva.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        categoriaeva = CategoriaEvaSerializer(categoriaeva, data=data, partial=True)
        if categoriaeva.is_valid():
            categoriaeva.save()
            return JSONResponse(categoriaeva.data)              
    elif request.method == "DELETE":
            #ya lo ley antes en el try
            categoriaeva.delete()
            return HttpResponse(status=400)
    return JSONResponse(categoriaeva.errors, status=400)


#######LLAMADO DE TABLA  ESTADO#########
#######LLAMADO DE TABLA  ESTADO#########
#######LLAMADO DE TABLA  ESTADO#########

@csrf_exempt ###metodo de llamado general
def rf_estado(request):
    if request.method == "GET":
        estado =  Estado.objects.all()
        serializer = EstadoSerializer(estado,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        estado = EstadoSerializer(data=data)
        if estado.is_valid():
            estado.save()
            return JSONResponse(estado.data, status=201)
    return JSONResponse(estado.errors, status=400)



@csrf_exempt ##metodo de llamado especifico
def rf_estado_reg(request, id_estado):
    try:
        estado = Estado.objects.get(pk=id_estado)
    except estado.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
          #ya lo ley antes en el try
         estado= EstadoSerializer(estado)
         return JSONResponse(estado.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        estado = EstadoSerializer(data=data)
        if estado.is_valid():
            estado.save()
            return JSONResponse(estado.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        estado = EstadoSerializer(estado, data=data, partial=True)
        if estado.is_valid():
            estado.save()
            return JSONResponse(estado.data)              
    elif request.method == "DELETE":
            #ya lo ley antes en el try
            estado.delete()
            return HttpResponse(status=400)
    return JSONResponse(estado.errors, status=400)


#######LLAMADO DE TABLA  FACTURA#########
#######LLAMADO DE TABLA  FACTURA#########
#######LLAMADO DE TABLA  FACTURA#########

@csrf_exempt ###metodo de llamado general
def rf_factura(request):
    if request.method == "GET":
        factura =  Factura.objects.all()
        serializer = FacturaSerializer(factura,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        factura = FacturaSerializer(data=data)
        if factura.is_valid():
            factura.save()
            return JSONResponse(factura.data, status=201)
    return JSONResponse(factura.errors, status=400)



@csrf_exempt ##metodo de llamado especifico
def rf_factura_reg(request, id_factura):
    try:
        factura = Factura.objects.get(pk=id_factura)
    except factura.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
          #ya lo ley antes en el try
         factura= FacturaSerializer(factura)
         return JSONResponse(factura.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        factura = FacturaSerializer(data=data)
        if factura.is_valid():
            factura.save()
            return JSONResponse(factura.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        factura = FacturaSerializer(factura, data=data, partial=True)
        if factura.is_valid():
            factura.save()
            return JSONResponse(factura.data)              
    elif request.method == "DELETE":
            #ya lo ley antes en el try
            factura.delete()
            return HttpResponse(status=400)
    return JSONResponse(factura.errors, status=400)



#######LLAMADO DE TABLA  GENERO#########
#######LLAMADO DE TABLA  GENERO#########
#######LLAMADO DE TABLA  GENERO#########

@csrf_exempt ###metodo de llamado general
def rf_genero(request):
    if request.method == "GET":
        genero =  Genero.objects.all()
        serializer = GeneroSerializer(genero,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        genero = GeneroSerializer(data=data)
        if genero.is_valid():
            genero.save()
            return JSONResponse(genero.data, status=201)
    return JSONResponse(genero.errors, status=400)



@csrf_exempt ##metodo de llamado especifico
def rf_genero_reg(request, id_genero):
    try:
        genero = Genero.objects.get(pk=id_genero)
    except genero.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
          #ya lo ley antes en el try
         genero= GeneroSerializer(genero)
         return JSONResponse(genero.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        genero = GeneroSerializer(data=data)
        if genero.is_valid():
            genero.save()
            return JSONResponse(genero.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        genero = GeneroSerializer(genero, data=data, partial=True)
        if genero.is_valid():
            genero.save()
            return JSONResponse(genero.data)              
    elif request.method == "DELETE":
            #ya lo ley antes en el try
            genero.delete()
            return HttpResponse(status=400)
    return JSONResponse(genero.errors, status=400)



#######LLAMADO DE TABLA  IDIOMA#########
#######LLAMADO DE TABLA  IDIOMA#########
#######LLAMADO DE TABLA  IDIOMA#########

@csrf_exempt ###metodo de llamado general
def rf_idioma(request):
    if request.method == "GET":
        idioma =  Idioma.objects.all()
        serializer = IdiomaSerializer(idioma,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        idioma = IdiomaSerializer(data=data)
        if idioma.is_valid():
            idioma.save()
            return JSONResponse(idioma.data, status=201)
    return JSONResponse(idioma.errors, status=400)



@csrf_exempt ##metodo de llamado especifico
def rf_idioma_reg(request, id_idioma):
    try:
        idioma = Idioma.objects.get(pk=id_idioma)
    except idioma.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
          #ya lo ley antes en el try
         idioma= IdiomaSerializer(idioma)
         return JSONResponse(idioma.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        idioma = IdiomaSerializer(data=data)
        if idioma.is_valid():
            idioma.save()
            return JSONResponse(idioma.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        idioma = IdiomaSerializer(idioma, data=data, partial=True)
        if idioma.is_valid():
            idioma.save()
            return JSONResponse(idioma.data)              
    elif request.method == "DELETE":
            #ya lo ley antes en el try
            idioma.delete()
            return HttpResponse(status=400)
    return JSONResponse(idioma.errors, status=400)



#######LLAMADO DE TABLA  PAIS#########
#######LLAMADO DE TABLA  PAIS#########
#######LLAMADO DE TABLA  PAIS#########

@csrf_exempt ###metodo de llamado general
def rf_pais(request):
    if request.method == "GET":
        pais =  Pais.objects.all()
        serializer = PaisSerializer(pais,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        pais = PaisSerializer(data=data)
        if pais.is_valid():
            pais.save()
            return JSONResponse(pais.data, status=201)
    return JSONResponse(pais.errors, status=400)



@csrf_exempt ##metodo de llamado especifico
def rf_pais_reg(request, id_pais):
    try:
        pais = Pais.objects.get(pk=id_pais)
    except pais.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
          #ya lo ley antes en el try
         pais= PaisSerializer(pais)
         return JSONResponse(pais.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        pais = PaisSerializer(data=data)
        if pais.is_valid():
            pais.save()
            return JSONResponse(pais.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        pais = PaisSerializer(pais, data=data, partial=True)
        if pais.is_valid():
            pais.save()
            return JSONResponse(pais.data)              
    elif request.method == "DELETE":
            #ya lo ley antes en el try
            pais.delete()
            return HttpResponse(status=400)
    return JSONResponse(pais.errors, status=400)


#######LLAMADO DE TABLA  rrss#########
#######LLAMADO DE TABLA  rrss#########
#######LLAMADO DE TABLA  rrss#########

@csrf_exempt ###metodo de llamado general
def rf_rrss(request):
    if request.method == "GET":
        rrss =  Rrss.objects.all()
        serializer = RrssSerializer(rrss,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        rrss = RrssSerializer(data=data)
        if rrss.is_valid():
            rrss.save()
            return JSONResponse(rrss.data, status=201)
    return JSONResponse(rrss.errors, status=400)



@csrf_exempt ##metodo de llamado especifico
def rf_rrss_reg(request, id_rrss):
    try:
        rrss = Rrss.objects.get(pk=id_rrss)
    except rrss.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
          #ya lo ley antes en el try
         rrss= RrssSerializer(rrss)
         return JSONResponse(rrss.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        rrss = RrssSerializer(data=data)
        if rrss.is_valid():
            rrss.save()
            return JSONResponse(rrss.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        rrss = RrssSerializer(rrss, data=data, partial=True)
        if rrss.is_valid():
            rrss.save()
            return JSONResponse(rrss.data)              
    elif request.method == "DELETE":
            #ya lo ley antes en el try
            rrss.delete()
            return HttpResponse(status=400)
    return JSONResponse(rrss.errors, status=400)

#######LLAMADO DE TABLA  TipoEmpresa#########
#######LLAMADO DE TABLA  TipoEmpresa#########
#######LLAMADO DE TABLA  TipoEmpresa#########

@csrf_exempt ###metodo de llamado general
def rf_tipoempresa(request):
    if request.method == "GET":
        tipoempresa =  TipoEmpresa.objects.all()
        serializer = TipoEmpresaSerializer(tipoempresa,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        tipoempresa = TipoEmpresaSerializer(data=data)
        if tipoempresa.is_valid():
            tipoempresa.save()
            return JSONResponse(tipoempresa.data, status=201)
    return JSONResponse(tipoempresa.errors, status=400)



@csrf_exempt ##metodo de llamado especifico
def rf_tipoempresa_reg(request, id_rrss):
    try:
        tipoempresa = TipoEmpresa.objects.get(pk=id_rrss)
    except tipoempresa.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
          #ya lo ley antes en el try
         tipoempresa= TipoEmpresaSerializer(tipoempresa)
         return JSONResponse(tipoempresa.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        tipoempresa = TipoEmpresaSerializer(data=data)
        if tipoempresa.is_valid():
            tipoempresa.save()
            return JSONResponse(tipoempresa.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        tipoempresa = TipoEmpresaSerializer(tipoempresa, data=data, partial=True)
        if tipoempresa.is_valid():
            tipoempresa.save()
            return JSONResponse(tipoempresa.data)              
    elif request.method == "DELETE":
            #ya lo ley antes en el try
            tipoempresa.delete()
            return HttpResponse(status=400)
    return JSONResponse(tipoempresa.errors, status=400)



#######LLAMADO DE TABLA  TipoGuia#########
#######LLAMADO DE TABLA  TipoGuia#########

@csrf_exempt ###metodo de llamado general
def rf_tipoguia(request):
    if request.method == "GET":
        tipoguia =  TipoGuia.objects.all()
        serializer = TipoGuiaSerializer(tipoguia,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        tipoguia = TipoGuiaSerializer(data=data)
        if tipoguia.is_valid():
            tipoguia.save()
            return JSONResponse(tipoguia.data, status=201)
    return JSONResponse(tipoguia.errors, status=400)

@csrf_exempt ##metodo de llamado especifico
def rf_tipoguia_reg(request, id_rrss):
    try:
        tipoguia = TipoGuia.objects.get(pk=id_rrss)
    except tipoguia.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
          #ya lo ley antes en el try
         tipoguia= TipoGuiaSerializer(tipoguia)
         return JSONResponse(tipoguia.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        tipoguia = TipoGuiaSerializer(data=data)
        if tipoguia.is_valid():
            tipoguia.save()
            return JSONResponse(tipoguia.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        tipoguia = TipoGuiaSerializer(tipoguia, data=data, partial=True)
        if tipoguia.is_valid():
            tipoguia.save()
            return JSONResponse(tipoguia.data)              
    elif request.method == "DELETE":
            #ya lo ley antes en el try
            tipoguia.delete()
            return HttpResponse(status=400)
    return JSONResponse(tipoguia.errors, status=400)


#######LLAMADO DE TABLA  Ciudad#########
#######LLAMADO DE TABLA  Ciudad#########
#######LLAMADO DE TABLA  Ciudad#########

@csrf_exempt
def rf_ciudad(request):
    if request.method == "GET":
        ciudades = Ciudad.objects.all()
        serializer = CiudadSerializer(ciudades, many=True)
        return JSONResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CiudadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def rf_ciudad_reg(request, id_ciudad, id_pais):
    try:
        ciudad = Ciudad.objects.get(pk=id_ciudad)
    except Ciudad.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        ciudad_serializer = CiudadSerializer(ciudad)
        return JSONResponse(ciudad_serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        data["id_pais"] = id_pais  # Asigna el ID del país correspondiente
        ciudad_serializer = CiudadSerializer(data=data)
        if ciudad_serializer.is_valid():
            ciudad_serializer.save()
            return JSONResponse(ciudad_serializer.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        ciudad_serializer = CiudadSerializer(ciudad, data=data, partial=True)
        if ciudad_serializer.is_valid():
            ciudad_serializer.save()
            return JSONResponse(ciudad_serializer.data)
    elif request.method == "DELETE":
        ciudad.delete()
        return HttpResponse(status=400)
    
    return JSONResponse(ciudad_serializer.errors, status=400)

#######LLAMADO DE TABLA  Cliente#########
#######LLAMADO DE TABLA  Cliente#########
#######LLAMADO DE TABLA  Cliente#########

@csrf_exempt
def rf_cliente(request):
    if request.method == "GET":
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return JSONResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClienteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def rf_cliente_reg(request, id_cliente, id_ciudad):
    try:
        cliente = Cliente.objects.get(pk=id_cliente)
    except Cliente.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        cliente_serializer = ClienteSerializer(cliente)
        return JSONResponse(cliente_serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        data["id_ciudad"] = id_ciudad  # Asigna el ID de ciudad correspondiente
        cliente_serializer = CiudadSerializer(data=data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return JSONResponse(cliente_serializer.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        cliente_serializer = CiudadSerializer(cliente, data=data, partial=True)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return JSONResponse(cliente_serializer.data)
    elif request.method == "DELETE":
        cliente.delete()
        return HttpResponse(status=400)
    
    return JSONResponse(cliente_serializer.errors, status=400)

#######LLAMADO DE TABLA  Empresa#########
#######LLAMADO DE TABLA  Empresa#########
#######LLAMADO DE TABLA  Empresa#########

@csrf_exempt
def rf_empresa(request):
    if request.method == "GET":
         empresa = Empresa.objects.all()
         serializer = EmpresaSerializer(empresa, many=True)
         return JSONResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmpresaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def rf_empresa_reg(request, id_empresa, id_tipo_empr, id_ciudad):
    try:
        empresa = Empresa.objects.get(pk=id_empresa)
    except Empresa.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        empresa_serializer = EmpresaSerializer(empresa)
        return JSONResponse(empresa_serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        data["id_tipo_empr"] = id_tipo_empr
        data["id_ciudad"] = id_ciudad  # Asigna el ID de ciudad correspondiente
        empresa_serializer = EmpresaSerializer(data=data)
        if empresa_serializer.is_valid():
            empresa_serializer.save()
            return JSONResponse(empresa_serializer.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        empresa_serializer = EmpresaSerializer(empresa, data=data, partial=True)
        if empresa_serializer.is_valid():
            empresa_serializer.save()
            return JSONResponse(empresa_serializer.data)
    elif request.method == "DELETE":
        empresa.delete()
        return HttpResponse(status=400)
    
    return JSONResponse(empresa_serializer.errors, status=400)

#######LLAMADO DE TABLA  Evaluación#########
#######LLAMADO DE TABLA  Evaluación#########
#######LLAMADO DE TABLA  Evaluación#########

@csrf_exempt
def rf_evaluacion(request):
    if request.method == "GET":
         evaluacion = Evaluacion.objects.all()
         serializer = EvaluacionSerializer(evaluacion, many=True)
         return JSONResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EvaluacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def rf_evaluacion_reg(request, id_eva_tour, id_cat_eva, id_rrss):
    try:
        evaluacion = Evaluacion.objects.get(pk=id_eva_tour)
    except Evaluacion.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        evaluacion_serializer = EvaluacionSerializer(evaluacion)
        return JSONResponse(evaluacion_serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        data["id_cat_eva"] = id_cat_eva
        data["id_rrss"] = id_rrss
        evaluacion_serializer = EvaluacionSerializer(data=data)
        if evaluacion_serializer.is_valid():
            evaluacion_serializer.save()
            return JSONResponse(evaluacion_serializer.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        evaluacion_serializer = EvaluacionSerializer(evaluacion, data=data, partial=True)
        if evaluacion_serializer.is_valid():
            evaluacion_serializer.save()
            return JSONResponse(evaluacion_serializer.data)
    elif request.method == "DELETE":
        evaluacion.delete()
        return HttpResponse(status=400)
    
    return JSONResponse(evaluacion_serializer.errors, status=400)

#######LLAMADO DE TABLA  PasajeroContacto#########
#######LLAMADO DE TABLA  PasajeroContacto#########
#######LLAMADO DE TABLA  PasajeroContacto#########

@csrf_exempt
def rf_pasajerocontacto(request):
    if request.method == "GET":
         pasajerocontacto = PasajeroContacto.objects.all()
         serializer = PasajeroContactoSerializer(pasajerocontacto, many=True)
         return JSONResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PasajeroContactoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def rf_pasajerocontacto_reg(request, id_pasaj, id_ciudad):
    try:
        pasajerocontacto = PasajeroContacto.objects.get(pk=id_pasaj)
    except PasajeroContacto.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        pasajerocontacto_serializer = PasajeroContactoSerializer(pasajerocontacto)
        return JSONResponse(pasajerocontacto_serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        data["id_ciudad"] = id_ciudad
        pasajerocontacto_serializer = PasajeroContactoSerializer(data=data)
        if pasajerocontacto_serializer.is_valid():
            pasajerocontacto_serializer.save()
            return JSONResponse(pasajerocontacto_serializer.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        pasajerocontacto_serializer = PasajeroContactoSerializer(pasajerocontacto, data=data, partial=True)
        if pasajerocontacto_serializer.is_valid():
            pasajerocontacto_serializer.save()
            return JSONResponse(pasajerocontacto_serializer.data)
    elif request.method == "DELETE":
        pasajerocontacto.delete()
        return HttpResponse(status=400)
    
    return JSONResponse(pasajerocontacto_serializer.errors, status=400)

#######LLAMADO DE TABLA  Tour#########
#######LLAMADO DE TABLA  Tour#########
#######LLAMADO DE TABLA  Tour#########

@csrf_exempt
def rf_tour(request):
    if request.method == "GET":
         tour = Tour.objects.all()
         serializer = TourSerializer(tour, many=True)
         return JSONResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TourSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def rf_tour_reg(request, id_tour, id_empresa, id_calidad, id_idioma):
    try:
        tour = Tour.objects.get(pk=id_tour)
    except Tour.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        tour_serializer = TourSerializer(tour)
        return JSONResponse(tour_serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        data["id_empresa"] = id_empresa
        data["id_calidad"] = id_calidad
        data["id_idioma"] = id_idioma
        tour_serializer = TourSerializer(data=data)
        if tour_serializer.is_valid():
            tour_serializer.save()
            return JSONResponse(tour_serializer.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        tour_serializer = TourSerializer(tour, data=data, partial=True)
        if tour_serializer.is_valid():
            tour_serializer.save()
            return JSONResponse(tour_serializer.data)
    elif request.method == "DELETE":
        tour.delete()
        return HttpResponse(status=400)
    
    return JSONResponse(tour_serializer.errors, status=400)

#######LLAMADO DE TABLA  TurnoTrabajo#########
#######LLAMADO DE TABLA  TurnoTrabajo#########
#######LLAMADO DE TABLA  TurnoTrabajo#########

@csrf_exempt
def rf_turnotrabajo(request):
    if request.method == "GET":
         turnotrabajo = TurnoTrabajo.objects.all()
         serializer = TurnoTrabajoSerializer(turnotrabajo, many=True)
         return JSONResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TurnoTrabajoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def rf_turnotrabajo_reg(request, id_turno, id_estado):
    try:
        turnotrabajo = TurnoTrabajo.objects.get(pk=id_turno)
    except TurnoTrabajo.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        turnotrabajo_serializer = TurnoTrabajoSerializer(turnotrabajo)
        return JSONResponse(turnotrabajo_serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        data["id_estado"] = id_estado
        turnotrabajo_serializer = TurnoTrabajoSerializer(data=data)
        if turnotrabajo_serializer.is_valid():
            turnotrabajo_serializer.save()
            return JSONResponse(turnotrabajo_serializer.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        turnotrabajo_serializer = TurnoTrabajoSerializer(turnotrabajo, data=data, partial=True)
        if turnotrabajo_serializer.is_valid():
            turnotrabajo_serializer.save()
            return JSONResponse(turnotrabajo_serializer.data)
    elif request.method == "DELETE":
        turnotrabajo.delete()
        return HttpResponse(status=400)
    
    return JSONResponse(turnotrabajo_serializer.errors, status=400)

#######LLAMADO DE TABLA  Horario#########
#######LLAMADO DE TABLA  Horario#########
#######LLAMADO DE TABLA  Horario#########

@csrf_exempt
def rf_horario(request):
    if request.method == "GET":
         horario = Horario.objects.all()
         serializer = HorarioSerializer(horario, many=True)
         return JSONResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HorarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def rf_horario_reg(request, id_horario, id_estado):
    try:
        horario = Horario.objects.get(pk=id_horario)
    except Horario.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        horario_serializer = HorarioSerializer(horario)
        return JSONResponse(horario_serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        data["id_estado"] = id_estado
        horario_serializer = HorarioSerializer(data=data)
        if horario_serializer.is_valid():
            horario_serializer.save()
            return JSONResponse(horario_serializer.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        horario_serializer = HorarioSerializer(horario, data=data, partial=True)
        if horario_serializer.is_valid():
            horario_serializer.save()
            return JSONResponse(horario_serializer.data)
    elif request.method == "DELETE":
        horario.delete()
        return HttpResponse(status=400)
    
    return JSONResponse(horario_serializer.errors, status=400)

#######LLAMADO DE TABLA  Itinerario#########
#######LLAMADO DE TABLA  Itinerario#########
#######LLAMADO DE TABLA  Itinerario#########

@csrf_exempt
def rf_itinerario(request):
    if request.method == "GET":
         itinerario = Itinerario.objects.all()
         serializer = ItinerarioSerializer(itinerario, many=True)
         return JSONResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItinerarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def rf_itinerario_reg(request, id_itinerario, id_estado):
    try:
        itinerario = Itinerario.objects.get(pk=id_itinerario)
    except Itinerario.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        itinerario_serializer = ItinerarioSerializer(itinerario)
        return JSONResponse(itinerario_serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        data["id_estado"] = id_estado
        itinerario_serializer = ItinerarioSerializer(data=data)
        if itinerario_serializer.is_valid():
            itinerario_serializer.save()
            return JSONResponse(itinerario_serializer.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        itinerario_serializer = ItinerarioSerializer(itinerario, data=data, partial=True)
        if itinerario_serializer.is_valid():
            itinerario_serializer.save()
            return JSONResponse(itinerario_serializer.data)
    elif request.method == "DELETE":
        itinerario.delete()
        return HttpResponse(status=400)
    return JSONResponse(itinerario_serializer.errors, status=400)

#######LLAMADO DE TABLA  Reserva#########
#######LLAMADO DE TABLA  Reserva#########
#######LLAMADO DE TABLA  Reserva#########

@csrf_exempt
def rf_reserva(request):
    if request.method == "GET":
         reserva = Reserva.objects.all()
         serializer = ReservaSerializer(reserva, many=True)
         return JSONResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReservaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def rf_reserva_reg(request, id_reserva, id_pasaj, id_tour):
    try:
        reserva = Reserva.objects.get(pk=id_reserva)
    except Reserva.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        reserva_serializer = ReservaSerializer(reserva)
        return JSONResponse(reserva_serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        data["id_pasaj"] = id_pasaj
        data["id_tour"] = id_tour
        reserva_serializer = ReservaSerializer(data=data)
        if reserva_serializer.is_valid():
            reserva_serializer.save()
            return JSONResponse(reserva_serializer.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        reserva_serializer = ReservaSerializer(reserva, data=data, partial=True)
        if reserva_serializer.is_valid():
            reserva_serializer.save()
            return JSONResponse(reserva_serializer.data)
    elif request.method == "DELETE":
        reserva.delete()
        return HttpResponse(status=400)
    return JSONResponse(reserva_serializer.errors, status=400)

#######LLAMADO DE TABLA  Guia#########
#######LLAMADO DE TABLA  Guia#########
#######LLAMADO DE TABLA  Guia#########

@csrf_exempt
def rf_guia(request):
    if request.method == "GET":
         guia = Guia.objects.all()
         serializer = GuiaSerializer(guia, many=True)
         return JSONResponse(guia.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GuiaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def rf_guia_reg(request, id_guia, id_pais, id_genero):
    try:
        guia = Guia.objects.get(pk=id_guia)
    except Guia.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        guia_serializer = GuiaSerializer(guia)
        return JSONResponse(guia_serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        data["id_pais"] = id_pais
        data["id_genero"] = id_genero
        guia_serializer = GuiaSerializer(data=data)
        if  guia_serializer.is_valid():
            guia_serializer.save()
            return JSONResponse(guia_serializer.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        guia_serializer = GuiaSerializer(guia, data=data, partial=True)
        if guia_serializer.is_valid():
            guia_serializer.save()
            return JSONResponse(guia_serializer.data)
    elif request.method == "DELETE":
        guia.delete()
        return HttpResponse(status=400)
    return JSONResponse(guia_serializer.errors, status=400)

#######LLAMADO DE TABLA  Guia#########
#######LLAMADO DE TABLA  Guia#########
#######LLAMADO DE TABLA  Guia#########

@csrf_exempt
def rf_guia(request):
    if request.method == "GET":
         guia = Guia.objects.all()
         serializer = GuiaSerializer(guia, many=True)
         return JSONResponse(guia.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GuiaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def rf_guia_reg(request, id_guia, id_pais, id_genero):
    try:
        guia = Guia.objects.get(pk=id_guia)
    except Guia.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        guia_serializer = GuiaSerializer(guia)
        return JSONResponse(guia_serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        data["id_pais"] = id_pais
        data["id_genero"] = id_genero
        guia_serializer = GuiaSerializer(data=data)
        if  guia_serializer.is_valid():
            guia_serializer.save()
            return JSONResponse(guia_serializer.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        guia_serializer = GuiaSerializer(guia, data=data, partial=True)
        if guia_serializer.is_valid():
            guia_serializer.save()
            return JSONResponse(guia_serializer.data)
    elif request.method == "DELETE":
        guia.delete()
        return HttpResponse(status=400)
    return JSONResponse(guia_serializer.errors, status=400)

#######LLAMADO DE TABLA  Usuario#########
#######LLAMADO DE TABLA  Usuario#########
#######LLAMADO DE TABLA  Usuario#########

@csrf_exempt
def rf_usuario(request):
    if request.method == "GET":
         usuario = Usuario.objects.all()
         serializer = UsuarioSerializer(usuario, many=True)
         return JSONResponse(usuario.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def rf_usuario_reg(request, id_usuario, id_empresa, id_cliente, id_pasaj, id_guia):
    try:
        usuario = Usuario.objects.get(pk=id_usuario)
    except Usuario.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        usuario_serializer = UsuarioSerializer(usuario)
        return JSONResponse(usuario_serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        data["id_empresa"] = id_empresa
        data["id_cliente"] = id_cliente
        data["id_pasaj"] = id_pasaj
        data["id_guia"] = id_guia
        usuario_serializer = UsuarioSerializer(data=data)
        if  usuario_serializer.is_valid():
            usuario_serializer.save()
            return JSONResponse(usuario_serializer.data, status=201)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(usuario, data=data, partial=True)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JSONResponse(usuario_serializer.data)
    elif request.method == "DELETE":
        usuario.delete()
        return HttpResponse(status=400)
    return JSONResponse(usuario_serializer.errors, status=400)