from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Persona(models.Model):
    rut = models.IntegerField(null=False, primary_key=True)
    dv = models.CharField(max_length=1, null=False)
    nombre = models.CharField(max_length=20)
    papellido = models.CharField(max_length=20, db_column="ap_pat")
    sapellido = models.CharField(max_length=20, db_column="ap_mat")
    contacto = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    def _str_(self):
        return self.rut


class Region(models.Model):  # steve
    cod_region = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
 
    # nombre + ' ' + self.papellido



###### tablas sin fk #######

class Contacto(models.Model):
    id_contacto = models.IntegerField(null=False, primary_key=True)
    nom_contacto = models.CharField(max_length=30)
    ape_contacto = models.CharField(max_length=30) 
    des_contacto = models.CharField(max_length=250)

    def __str__(self):
        return self.nom_contacto, self.ape_contacto, self.des_contacto
    

class CalidadTour(models.Model):
    id_calidad = models.IntegerField(null=False, primary_key=True)
    des_calidad = models.CharField(max_length=100)

    def __str__(self):
        return self.des_calidad


class CategoriaEva(models.Model):
    id_cat_eva = models.IntegerField(null=False, primary_key=True)
    nom_cate = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_cate

class Estado(models.Model):
    id_estado = models.IntegerField(null=False, primary_key=True)
    des_estado = models.CharField(max_length=100)

    def __str__(self):
        return self.des_estado

class Factura(models.Model):
    id_factura = models.IntegerField(null=False, primary_key=True)
    fecha = models.CharField(max_length=10, null=False)
    porc_factura = models.CharField(max_length=2)
    porc_iva = models.CharField(max_length=2)
    monto_iva = models.CharField(max_length=200)

    def __str__(self):
        return self.id_factura

class Genero(models.Model):
    id_genero = models.IntegerField(null=False, primary_key=True)
    des_genero = models.CharField(max_length=100)

    def __str__(self):
        return self.des_genero

class Idioma(models.Model):
    id_idioma = models.IntegerField(null=False, primary_key=True)
    des_idioma = models.CharField(max_length=100)

    def __str__(self):
        return self.des_idioma

class Pais(models.Model):
    id_pais = models.IntegerField(null=False, primary_key=True)
    nom_pais = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)    

    def __str__(self):
        return self.nom_pais, self.nacionalidad    


class Rrss(models.Model):
    id_rrss = models.IntegerField(null=False, primary_key=True)
    nom_rrss = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_rrss

class TipoEmpresa(models.Model):
    id_tipo_empr = models.IntegerField(null=False, primary_key=True)
    des_tipo_empr = models.CharField(max_length=100)

    def __str__(self):
        return self.des_tipo_empr

class TipoGuia(models.Model):
    id_tip_guia = models.IntegerField(null=False, primary_key=True)
    nom_tipo_guia = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_tipo_guia



###### tablas con pk y fk ########



class Ciudad(models.Model):
    id_ciudad = models.IntegerField(null=False, primary_key=True)
    nom_ciu = models.CharField(max_length=100)
    id_pais = models.ForeignKey(Pais,on_delete=models.CASCADE,default=0)    

    def __str__(self):
        return self.nom_ciu

class Cliente(models.Model):
    id_cliente = models.IntegerField(null=False, primary_key=True)
    dni = models.CharField(max_length=10, null=False)
    nom_user = models.CharField(max_length=20)
    pape_user = models.CharField(max_length=20,db_column='ap_pat')
    sape_user = models.CharField(max_length=20,db_column='ap_mat')
    contacto = models.CharField(max_length=30)
    direccion = models.TextField(default=0)
    email = models.EmailField(max_length=50)
    #timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    #clave = models.CharField(max_length=10)
    id_ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE,default=0)  

    def _str_(self):
        return self.id_cliente
    #nombre + ' ' + self.papellido


class Empresa(models.Model):
    id_empresa = models.IntegerField(null=False, primary_key=True)
    nom_empresa = models.CharField(max_length=20)
    rut_empr = models.CharField(max_length=10, null=False)
    email_empr = models.EmailField(max_length=50)
    contacto_empr = models.CharField(max_length=30)
    direccion_empr = models.TextField(default=0)
    representante = models.CharField(max_length=30)
    nom_dueño = models.CharField(max_length=20)
    rut_dueño = models.CharField(max_length=10, null=False)
    contacto_dueño = models.CharField(max_length=30)
    email_dueño = models.EmailField(max_length=50)
    id_tipo_empr = models.ForeignKey(TipoEmpresa,on_delete=models.CASCADE,default=0)
    id_ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE,default=0)   

    def _str_(self):
        return self.id_empresa

class Evaluacion(models.Model):
    id_eva_tour = models.IntegerField(null=False, primary_key=True)
    opinion = models.TextField(default=0)
    puntos = models.CharField(max_length=5, null=False)
    nota = models.CharField(max_length=5, null=False)
    nom_eva = models.CharField(max_length=20)
    pape_user = models.CharField(max_length=20)
    email_eva = models.EmailField(max_length=50)
    id_cat_eva = models.ForeignKey(CategoriaEva,on_delete=models.CASCADE,default=0)
    id_rrss = models.ForeignKey(Rrss,on_delete=models.CASCADE,default=0)   

    def _str_(self):
        return self.id_eva_tour

class PasajeroContacto(models.Model):
    id_pasaj = models.IntegerField(null=False, primary_key=True)
    dni = models.CharField(max_length=10, null=False)
    nom_pasaj = models.CharField(max_length=20)
    ap_pasaj = models.CharField(max_length=30,db_column='apellidos')
    fono = models.CharField(max_length=30)
    email_pasaj = models.EmailField(max_length=50)
    id_ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE,default=0) 

    def _str_(self):
        return self.id_pasaj


class Tour(models.Model):
    id_tour = models.IntegerField(null=False, primary_key=True)
    nom_tour = models.CharField(max_length=20)
    fecha_tour = models.CharField(max_length=10)
    desc_tour = models.TextField(default=0)
    valor_tour = models.CharField(max_length=7)
    id_empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE,default=0) 
    id_calidad = models.ForeignKey(CalidadTour,on_delete=models.CASCADE,default=0)
    id_idioma = models.ForeignKey(Idioma,on_delete=models.CASCADE,default=0) 
 
    def _str_(self):
        return self.id_tour


class TurnoTrabajo(models.Model):
    id_turno = models.IntegerField(null=False, primary_key=True)
    desc_horario = models.CharField(max_length=20)
    tramo_ini = models.CharField(max_length=5)
    tramo_fin = models.CharField(max_length=5)
    id_estado = models.ForeignKey(Estado,on_delete=models.CASCADE,default=0) 
 
    def _str_(self):
        return self.desc_horario

class Horario(models.Model):
    id_horario = models.IntegerField(null=False, primary_key=True)
    hora = models.CharField(max_length=5)
    des_horario = models.CharField(max_length=100)
    id_estado = models.ForeignKey(Estado,on_delete=models.CASCADE,default=0)
    
    def __str__(self):
        return self.hora

class Itinerario(models.Model):
    id_itinerario = models.IntegerField(null=False, primary_key=True)
    nom_reco = models.CharField(max_length=25, null=False)
    desc_reco = models.TextField(default=0)
    ini_reco = models.CharField(max_length=20)
    fin_reco = models.CharField(max_length=20)
    duracion = models.CharField(max_length=3)
    unidad = models.CharField(max_length=3)
    #mapa_iti = imagen del mapa o mapa de google
    id_estado = models.ForeignKey(Estado,on_delete=models.CASCADE,default=0)
    
    def _str_(self):
        return self.id_itinerario

class Reserva(models.Model):
    id_reserva = models.IntegerField(null=False, primary_key=True)
    desc_general_tour = models.TextField(default=0)
    cant_niño = models.CharField(max_length=2)
    cant_adolescente = models.CharField(max_length=2)
    cant_adulto = models.CharField(max_length=2)
    cant_senior = models.CharField(max_length=2)
    tot_cant = models.CharField(max_length=2)
    id_pasaj = models.ForeignKey(PasajeroContacto,on_delete=models.CASCADE,default=0) 
    id_tour = models.ForeignKey(Tour,on_delete=models.CASCADE,default=0) 

    def _str_(self):
        return self.id_reserva



class DetalleReserva(models.Model):
    id_det_reserva = models.IntegerField(null=False, primary_key=True)
    id_ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE,default=0)
    id_reserva = models.ForeignKey(Reserva,on_delete=models.CASCADE,default=0) 
    id_estado =  models.ForeignKey(Estado,on_delete=models.CASCADE,default=0)
    id_cliente =  models.ForeignKey(Cliente,on_delete=models.CASCADE,default=0) 
    monto_reserva = models.CharField(max_length=200, null=True)

    def _str_(self):
        return self.id_det_reserva

class DetalleFac(models.Model):
    id_det_fac = models.IntegerField(null=False, primary_key=True)
    fech_fac = models.CharField(max_length=10, null=False)
    tot_fac = models.CharField(max_length=200, null=False)
    monto_iv = models.CharField(max_length=200, null=False)
    monto_neto = models.CharField(max_length=200, null=False)
    id_factura = models.ForeignKey(Factura,on_delete=models.CASCADE,default=0) 
    id_det_reserva = models.ForeignKey(DetalleReserva,on_delete=models.CASCADE,default=0) 

    def _str_(self):
        return self.id_det_fac

class DetalleTour(models.Model):
    id_det_tour = models.IntegerField(null=False, primary_key=True)
    id_horario = models.ForeignKey(Horario,on_delete=models.CASCADE,default=0)
    id_itinerario = models.ForeignKey(Itinerario,on_delete=models.CASCADE,default=0)
    id_tour = models.ForeignKey(Tour,on_delete=models.CASCADE,default=0)
    id_idioma = models.ForeignKey(Idioma,on_delete=models.CASCADE,default=0)
    id_eva_tour = models.ForeignKey(Evaluacion,on_delete=models.CASCADE,default=0)
    id_ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE,default=0)    
    def _str_(self):
        return self.id_det_tour


class Guia(models.Model):
    id_guia = models.IntegerField(null=False, primary_key=True)
    dni = models.CharField(max_length=10, null=False)
    nom_guia = models.CharField(max_length=20)
    pape_guia = models.CharField(max_length=20,db_column='ap_pat')
    sape_guia = models.CharField(max_length=20,db_column='ap_mat')
    contacto_guia = models.CharField(max_length=30)
    fnac_guia = models.CharField(max_length=10)
    email_guia = models.EmailField(max_length=50)
    id_pais = models.ForeignKey(Pais,on_delete=models.CASCADE,default=0)  
    id_genero = models.ForeignKey(Genero,on_delete=models.CASCADE,default=0)

    def _str_(self):
        return self.id_guia

class DetalleGuia(models.Model):
    id_det_guia = models.IntegerField(null=False, primary_key=True)
    nom_horario_guia = models.CharField(max_length=100, null=False)
    id_guia = models.ForeignKey(Guia,on_delete=models.CASCADE,default=0)
    id_tip_guia = models.ForeignKey(TipoGuia,on_delete=models.CASCADE,default=0) 
    id_idioma = models.ForeignKey(Idioma,on_delete=models.CASCADE,default=0)  

    def _str_(self):
        return self.id_det_guia

class Usuario(models.Model):
    id_usuario = models.IntegerField(null=False, primary_key=True)
    mail = models.CharField(max_length=30)
    password = models.CharField(max_length=8)
    id_empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE,default=0)
    id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,default=0)
    id_pasaj = models.ForeignKey(PasajeroContacto,on_delete=models.CASCADE,default=0)
    id_guia = models.ForeignKey(Guia,on_delete=models.CASCADE,default=0)    

    def __str__(self):
        return self.mail
  




