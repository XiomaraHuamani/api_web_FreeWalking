from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import *


class HarrysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"
        # fields = ('rut', 'dv', 'nombre', 'papellido', 'sapellido', 'contacto', 'email')
        # fields = ('question','id')


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("cod_region", "nombre")
 

###### tablas sin fk #######

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ("id_contacto", "nom_contacto", "ape_contacto", "des_contacto")

class CalidadTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalidadTour
        fields = ("id_calidad", "des_calidad")


class CategoriaEvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaEva
        fields = ("id_cat_eva", "nom_cate")


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ("id_estado", "des_estado")


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ("id_factura", "fecha","porc_factura","porc_iva","monto_iva")


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ("id_genero", "des_genero")        


class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = ("id_idioma", "des_idioma")  


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ("id_pais", "nom_pais","nacionalidad")  

class RrssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rrss
        fields = ("id_rrss", "nom_rrss")  

class TipoEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEmpresa
        fields = ("id_tipo_empr", "des_tipo_empr") 

class TipoGuiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoGuia
        fields = ("id_tip_guia", "nom_tipo_guia")          

###### tablas con pk y fk ########

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ("id_ciudad", "nom_ciu", "id_pais") 

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ("id_cliente", "dni", "nom_user", "pape_user", "sape_user", "contacto", 
                  "direccion", "email", "id_ciudad")
	# fields = ("timestamp", "clave")

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ("id_empresa", "nom_empresa", "rut_empr", "email_empr", "contacto_empr", 
                  "direccion_empr", "representante", "nom_dueño", "rut_dueño", 
                  "contacto_dueño", "contacto_dueño",
                   "id_tipo_empr", "id_ciudad")

class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = ("id_eva_tour", "opinion", "puntos", "nota", "nom_eva", "pape_user", 
                  "email_eva", "id_cat_eva", "id_rrss")

class PasajeroContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasajeroContacto
        fields = ("id_pasaj", "dni", "nom_pasaj", "ape_pasaj", "fono"
                  , "email_pasaj", "id_ciudad")

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ("id_tour", "nom_tour", "fecha_tour", "desc_tour"
                  , "valor_tour", "id_empresa", "id_calidad", "id_idioma") 

class TurnoTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurnoTrabajo
        fields = ("id_turno", "desc_horario", "tramo_ini", "tramo_fin", "id_estado") 

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ("id_horario", "hora", "des_horario", "id_estado")


class ItinerarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerario
        fields = ("id_itinerario", "nom_reco", "desc_reco", "ini_reco", 
                  "fin_reco", "duracion", "unidad", "id_estado")
	#fields = ("mapa_iti")
	
class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ("id_reserva", "desc_general_tour", "cant_niño", "cant_adolescente"
                  , "cant_adulto", "cant_senior", "tot_cant", "id_pasaj", "id_tour")

class DetalleReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleReserva
        fields = ("id_det_reserva", "id_ciudad", "id_reserva", "id_estado", "id_cliente")

class DetalleFacSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleFac
        fields = ("id_det_fac", "fech_fac", "tot_fac", "monto_iv", "monto_neto"
                  , "id_factura", "id_det_reserva")

class DetalleTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleTour
        fields = ("id_det_tour", "id_horario", "id_itinerario", "id_tour", "id_idioma"
                  , "id_eva_tour", "id_ciudad")

class GuiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guia
        fields = ("id_guia", "dni", "nom_guia", "pape_guia", "sape_guia", "contacto_guia"
                  , "fnac_guia", "email_guia", "id_pais", "id_genero")

class DetalleGuiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleGuia
        fields = ("id_det_guia", "nom_horario_guia", "id_guia", "id_tip_guia", "id_idioma")

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("id_usuario", "mail", "password", "id_empresa", "id_cliente"
                  , "id_pasaj", "id_guia")
