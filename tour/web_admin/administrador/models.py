from django.db import models

###### tablas sin fk #######

# Contacto pag, admin listar


class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    nom_contacto = models.CharField(max_length=30)
    ape_contacto = models.CharField(max_length=30)
    email_contacto = models.EmailField(max_length=50)
    fono_contacto = models.IntegerField(null=True)
    mensaje = models.CharField(max_length=250)

    class Meta:
        db_table = 'contacto'


"""class CalidadTour(models.Model):
    id_calidad = models.AutoField(primary_key=True)
    des_calidad = models.CharField(max_length=100)

    class Meta:
        db_table = 'calidad_tour'"""

"""class CategoriaEva(models.Model):
    id_cat_eva = models.AutoField(primary_key=True)
    nom_cate = models.CharField(max_length=100)

    class Meta:
        db_table = 'categoria_eva'"""

# Bruto


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    des_estado = models.CharField(max_length=100)

    class Meta:
        db_table = 'estado'

# Factura ya ingresada


class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=10, null=False)
    porc_factura = models.IntegerField(null=True)
    porc_iva = models.IntegerField(null=True)
    monto_iva = models.IntegerField(null=True)

    class Meta:
        db_table = 'factura'


# Bruto
"""class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    des_genero = models.CharField(max_length=100)

    class Meta:
        db_table = 'genero'"""

# Bruto


class Idioma(models.Model):
    id_idioma = models.AutoField(primary_key=True)
    des_idioma = models.CharField(max_length=100)

    class Meta:
        db_table = 'idioma'

# Bruto


class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nom_pais = models.CharField(max_length=100)
    # nacionalidad = models.CharField(max_length=100)

    class Meta:
        db_table = 'pais'


"""class Rrss(models.Model):
    id_rrss = models.AutoField(primary_key=True)
    nom_rrss = models.CharField(max_length=100)

    class Meta:
        db_table = 'rrss'"""


"""class TipoEmpresa(models.Model):
    id_tipo_empr = models.AutoField(primary_key=True)
    des_tipo_empr = models.CharField(max_length=100)

    class Meta:
        db_table = 'tipo_empresa'"""

"""class TipoGuia(models.Model):
    id_tip_guia = models.AutoField(primary_key=True)
    nom_tipo_guia = models.CharField(max_length=100)

    class Meta:
        db_table = 'tipo_guia'"""


###### tablas con pk y fk ########


# Bruto
class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    nom_ciu = models.CharField(max_length=100)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=0)

    class Meta:
        db_table = 'ciudad'


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=10, null=False)
    username = models.CharField(max_length=20)
    ape_pat = models.CharField(max_length=20, db_column='ap_pat')
    ape_mat = models.CharField(max_length=20, db_column='ap_mat')
    genero = models.CharField(max_length=10)
    contacto = models.CharField(max_length=30)
    direccion = models.TextField(default=0)
    email = models.EmailField(max_length=50)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=0)

    class Meta:
        db_table = 'cliente'


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
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
    # id_tipo_empr = models.ForeignKey(TipoEmpresa,on_delete=models.CASCADE,default=0)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=0)

    class Meta:
        db_table = 'empresa'


"""class Evaluacion(models.Model):
    id_eva = models.AutoField(primary_key=True)
    opinion = models.TextField(default=0)
    puntos = models.IntegerField(null=True)
    nota = models.IntegerField(null=True)
    nom_eva = models.CharField(max_length=20)
    ape_eva = models.CharField(max_length=20)
    email_eva = models.EmailField(max_length=50)
    id_cat_eva = models.ForeignKey(CategoriaEva,on_delete=models.CASCADE,default=0)
    id_rrss = models.ForeignKey(Rrss,on_delete=models.CASCADE,default=0)   

    class Meta:
        db_table = 'evaluacion'"""


class PasajeroContacto(models.Model):
    id_pasaj = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=10, null=False)
    nom_pasaj = models.CharField(max_length=20)
    ap_pasaj = models.CharField(max_length=30, db_column='apellidos')
    fono = models.IntegerField(null=True)
    email_pasaj = models.EmailField(max_length=50)
    ciudad = models.CharField(max_length=10, null=False)

    class Meta:
        db_table = 'pasajero_contacto'


class Tour(models.Model):
    id_tour = models.AutoField(primary_key=True)
    nom_tour = models.CharField(max_length=20)
    fecha_tour = models.CharField(max_length=10)
    desc_tour = models.TextField(default=0)
    valor_tour = models.IntegerField(null=True)
    # id_empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE,default=0,  null= True)
    # id_calidad = models.ForeignKey(CalidadTour,on_delete=models.CASCADE,default=0)
    # id_idioma = models.ForeignKey(Idioma,on_delete=models.CASCADE,default=0)

    class Meta:
        db_table = 'tour'


class TurnoTrabajo(models.Model):
    id_turno = models.AutoField(primary_key=True)
    desc_horario = models.CharField(max_length=20)
    tramo_ini = models.CharField(max_length=5)
    tramo_fin = models.CharField(max_length=5)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=0)

    class Meta:
        db_table = 'turno_trabajo'

# Bruto


class Horario(models.Model):
    id_horario = models.AutoField(primary_key=True)
    hora = models.CharField(max_length=15)
    duracion = models.IntegerField(null=True)
    modo = models.CharField(max_length=100)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=0)

    class Meta:
        db_table = 'horario'


"""class Itinerario(models.Model):
    id_itinerario = models.AutoField(primary_key=True)
    nom_reco = models.CharField(max_length=25, null=False)
    desc_reco = models.TextField(default=0)
    ini_reco = models.CharField(max_length=20)
    fin_reco = models.CharField(max_length=20)
    duracion = models.CharField(max_length=3)
    unidad = models.CharField(max_length=3)
    #mapa_iti = imagen del mapa o mapa de google
    id_estado = models.ForeignKey(Estado,on_delete=models.CASCADE,default=0)
    
    class Meta:
       db_table = 'itinerario'"""


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    cant_nino = models.IntegerField(null=True)
    cant_adulto = models.IntegerField(null=False)
    tot_cant = models.IntegerField(null=False)
    id_pasaj = models.ForeignKey(
        PasajeroContacto, on_delete=models.CASCADE, default=0)
    id_tour = models.ForeignKey(Tour, on_delete=models.CASCADE, default=0)

    class Meta:
        db_table = 'reserva'


class DetalleReserva(models.Model):
    id_det_reserva = models.AutoField(primary_key=True)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=0)
    id_reserva = models.ForeignKey(
        Reserva, on_delete=models.CASCADE, default=0)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=0)
    id_cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, default=0)
    monto_reserva = models.IntegerField(null=True)

    class Meta:
        db_table = 'detalle_reserva'


class DetalleFac(models.Model):
    id_det_fac = models.AutoField(primary_key=True)
    fech_fac = models.DateTimeField(auto_now_add=True)  # automatica
    # monto_iva = models.IntegerField(null=True)
    # monto_neto = models.IntegerField(null=True)
    tot_fac = models.IntegerField(null=True)
    id_factura = models.ForeignKey(
        Factura, on_delete=models.CASCADE, default=0)
    id_det_reserva = models.ForeignKey(
        DetalleReserva, on_delete=models.CASCADE, default=0)

    class Meta:
        db_table = 'detalle_fac'

# Por Admin


class Guia(models.Model):
    id_guia = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=10, null=False)
    nom_guia = models.CharField(max_length=20)
    pape_guia = models.CharField(max_length=20, db_column='ap_pat')
    sape_guia = models.CharField(max_length=20, db_column='ap_mat')
    contacto_guia = models.CharField(max_length=30)
    fnac_guia = models.CharField(max_length=10)
    email_guia = models.EmailField(max_length=50)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=0)
    # id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE, default=0)

    class Meta:
        db_table = 'guia'


class DetalleGuia(models.Model):
    id_det_guia = models.AutoField(primary_key=True)
    nom_horario_guia = models.CharField(max_length=100, null=False)
    id_guia = models.ForeignKey(Guia, on_delete=models.CASCADE, default=0)
    # id_tip_guia = models.ForeignKey(TipoGuia,on_delete=models.CASCADE,default=0)
    id_idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE, default=0)

    class Meta:
        db_table = 'detalle_guia'


class DetalleTour(models.Model):
    id_det_tour = models.AutoField(primary_key=True)
    id_horario = models.ForeignKey(
        Horario, on_delete=models.CASCADE, default=0)
    # id_itinerario = models.ForeignKey(Itinerario, on_delete=models.CASCADE, default=0)
    id_tour = models.ForeignKey(Tour, on_delete=models.CASCADE, default=0)
    # id_idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE, default=0)
    id_ciudad = models.ForeignKey(
        Ciudad, on_delete=models.CASCADE, default=0, related_name='detalles_ciudad')
    id_guia = models.ForeignKey(
        Guia, on_delete=models.CASCADE, default=0, related_name='detalles_guia')

    class Meta:
        db_table = 'detalle_tour'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    mail = models.CharField(max_length=30)
    clave = models.CharField(max_length=10)
    # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    # id_empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE,default=0)
    # id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,default=0)
    # id_pasaj = models.ForeignKey(PasajeroContacto,on_delete=models.CASCADE,default=0)
    # id_guia = models.ForeignKey(Guia,on_delete=models.CASCADE,default=0)

    class Meta:
        db_table = 'usuarios'
