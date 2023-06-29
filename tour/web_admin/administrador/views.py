from django.shortcuts import render
from django.urls import path
from django import views
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .views import *
from django.template import loader

# Create your views here.


# Create your views here.
 

def index(request):  # <<==========
    return render(request, "index.html")  # <<==========


def home_index(request):
    template = loader.get_template('home_index.html')
    return HttpResponse(template.render())


def tours(request):
    template = loader.get_template('tours.html')
    return HttpResponse(template.render())


def acerca_de(request):
    template = loader.get_template('acerca_de.html')
    return HttpResponse(template.render())


def elements(request):
    template = loader.get_template('elements.html')
    return HttpResponse(template.render())


def contacto(request):
    template = loader.get_template('contacto.html')
    return HttpResponse(template.render())


def index2(request):
    template = loader.get_template('index2.html')
    return HttpResponse(template.render())


def reserva_tour(request):
    template = loader.get_template('reserva_tour.html')
    return HttpResponse(template.render())


def registro_cliente(request):
    template = loader.get_template('registro_cliente.html')
    return HttpResponse(template.render())


def pago_tour(request):
    template = loader.get_template('pago_tour.html')
    return HttpResponse(template.render())


def pago_final(request):
    template = loader.get_template('pago_final.html')
    return HttpResponse(template.render())

######## USUARIO################################


def actualizar(request):
    if request.method == "POST":
        if (
            request.POST.get('id_usuario')
            and request.POST.get('username')
            and request.POST.get('mail')
            and request.POST.get('clave')
        ):
            # Obtener el objeto de usuario a actualizar
            user = Usuarios.objects.get(
                id_usuario=request.POST.get('id_usuario'))

            # Actualizar los campos necesarios
            user.username = request.POST.get('username')
            user.mail = request.POST.get('mail')
            user.clave = request.POST.get('clave')

            # Guardar los cambios en la base de datos
            user.save()

            return redirect('listar')
    else:
        users = Usuarios.objects.all()
        datos = {'usuarios': users}
        return render(request, "Usuarios_/actualizar.html", datos)


def agregar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        mail = request.POST.get('mail')
        clave = request.POST.get('clave')

        # Imprime los valores de los campos para depurar
        print(username, mail, clave)

        if username and mail and clave:
            user = Usuarios()
            user.username = username
            user.mail = mail
            user.clave = clave
            user.save()
            return redirect('listar')
        else:
            return HttpResponse("Faltan datos en el formulario")
    else:
        return render(request, "Usuarios_/agregar.html")


def eliminar(request):
    if request.method == 'POST':
        if request.POST.get('id_usuario'):
            id_a_borrar = request.POST.get('id_usuario')
            try:
                usuarios = Usuarios.objects.get(id_usuario=id_a_borrar)
                usuarios.delete()
                return redirect('listar')
            except Usuarios.DoesNotExist:
                return redirect('listar')
    else:
        usuarios = Usuarios.objects.all()
        datos = {'usuarios': usuarios}
        return render(request, "Usuarios_/eliminar.html", datos)


def listar(request):
    users = Usuarios.objects.all()
    datos = {'usuarios': users}
    return render(request, "Usuarios_/listar.html", datos)


############## GUIA ##################

def actualizarGuia(request):
    if request.method == "POST":
        if (
            request.POST.get('id_guia')
            and request.POST.get('dni')
            and request.POST.get('nom_guia')
            and request.POST.get('pape_guia')
            and request.POST.get('sape_guia')
            and request.POST.get('contacto_guia')
            and request.POST.get('fnac_guia')
            and request.POST.get('email_guia')
            and request.POST.get('id_pais')
        ):
            # Obtener el objeto de usuario a actualizar
            user = Guia.objects.get(id_guia=request.POST.get('id_guia'))

            # Actualizar los campos necesarios
            user.dni = request.POST.get('dni')
            user.nom_guia = request.POST.get('nom_guia')
            user.pape_guia = request.POST.get('pape_guia')
            user.sape_guia = request.POST.get('sape_guia')
            user.contacto_guia = request.POST.get('contacto_guia')
            user.fnac_guia = request.POST.get('fnac_guia')
            user.email_guia = request.POST.get('email_guia')

            # Obtener la instancia de Pais correspondiente
            pais_id = request.POST.get('id_pais')
            pais = Pais.objects.get(id_pais=pais_id)
            user.id_pais = pais

            # Guardar los cambios en la base de datos
            user.save()

            return redirect('listarGuia')
    else:
        users = Guia.objects.all()
        datos = {'guia': users}
        return render(request, "Guia/actualizarGuia.html", datos)


def agregarGuia(request):
    if request.method == 'POST':
        dni = request.POST.get('dni')
        nom_guia = request.POST.get('nom_guia')
        pape_guia = request.POST.get('pape_guia')
        sape_guia = request.POST.get('sape_guia')
        contacto_guia = request.POST.get('contacto_guia')
        fnac_guia = request.POST.get('fnac_guia')
        email_guia = request.POST.get('email_guia')
        id_pais = request.POST.get('id_pais')

        # Imprime los valores de los campos para depurar
        print(dni, nom_guia, pape_guia, sape_guia, contacto_guia,
              fnac_guia, email_guia, id_pais)

        if dni and nom_guia and pape_guia and sape_guia and contacto_guia and fnac_guia and email_guia and id_pais:
            pais = get_object_or_404(Pais, id_pais=id_pais)
            user = Guia()
            user.dni = dni
            user.nom_guia = nom_guia
            user.pape_guia = pape_guia
            user.sape_guia = sape_guia
            user.contacto_guia = contacto_guia
            user.fnac_guia = fnac_guia
            user.email_guia = email_guia
            user.id_pais = pais
            user.save()
            return redirect('listarGuia')
        else:
            return HttpResponse("Faltan datos en el formulario")
    else:
        return render(request, "Guia/agregarGuia.html")


def eliminarGuia(request):
    if request.method == 'POST':
        if request.POST.get('id_guia'):
            id_a_borrar = request.POST.get('id_guia')
            try:
                usuario = Guia.objects.get(id_guia=id_a_borrar)
                usuario.delete()
                return redirect('listarGuia')
            except Guia.DoesNotExist:
                return redirect('listarGuia')
    else:
        users = Guia.objects.all()
        datos = {'guia': users}
        return render(request, "Guia/eliminarGuia.html", datos)


def listarGuia(request):
    users = Guia.objects.all()
    datos = {'guia': users}
    return render(request, "Guia/listarGuia.html", datos)


################## FACTURA ################

def actualizarFactura(request):
    if request.method == "POST":
        if (
            request.POST.get('id_factura')
            and request.POST.get('fecha')
            and request.POST.get('porc_factura')
            and request.POST.get('porc_iva')
            and request.POST.get('monto_iva')
        ):
            # Obtener el objeto de usuario a actualizar
            user = Factura.objects.get(
                id_factura=request.POST.get('id_factura'))

            # Actualizar los campos necesarios
            user.fecha = request.POST.get('fecha')
            user.porc_factura = request.POST.get('porc_factura')
            user.porc_iva = request.POST.get('porc_iva')
            user.monto_iva = request.POST.get('monto_iva')

            # Guardar los cambios en la base de datos
            user.save()

            return redirect('listarFactura')
    else:
        users = Factura.objects.all()
        datos = {'factura': users}
        return render(request, "Factura/actualizarFactura.html", datos)


def agregarFactura(request):
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        porc_factura = request.POST.get('porc_factura')
        porc_iva = request.POST.get('porc_iva')
        monto_iva = request.POST.get('monto_iva')

        # Imprime los valores de los campos para depurar
        print(fecha, porc_factura, porc_iva, monto_iva)

        if fecha and porc_factura and porc_iva and monto_iva:
            user = Factura()
            user.fecha = fecha
            user.porc_factura = porc_factura
            user.porc_iva = porc_iva
            user.monto_iva = monto_iva
            user.save()
            return redirect('listarFactura')
        else:
            return HttpResponse("Faltan datos en el formulario")
    else:
        return render(request, "Factura/agregarFactura.html")


def eliminarFactura(request):
    if request.method == 'POST':
        if request.POST.get('id_factura'):
            id_a_borrar = request.POST.get('id_factura')
            try:
                usuario = Factura.objects.get(id_factura=id_a_borrar)
                usuario.delete()
                return redirect('listarFactura')
            except Factura.DoesNotExist:
                return redirect('listarFactura')
    else:
        users = Factura.objects.all()
        datos = {'factura': users}
        return render(request, "Factura/eliminarFactura.html", datos)


def listarFactura(request):
    users = Factura.objects.all()
    datos = {'factura': users}
    return render(request, "Factura/listarFactura.html", datos)


################## CLIENTE ################

def actualizarCliente(request):
    if request.method == "POST":
        if (
            request.POST.get('id_cliente')
            and request.POST.get('dni')
            and request.POST.get('nom_user')
            and request.POST.get('ape_pat')
            and request.POST.get('ape_mat')
            and request.POST.get('genero')
            and request.POST.get('contacto')
            and request.POST.get('direccion')
            and request.POST.get('email')
            and request.POST.get('id_ciudad')
        ):
            # Obtener el objeto de usuario a actualizar
            user = Cliente.objects.get(
                id_cliente=request.POST.get('id_cliente'))

            # Actualizar los campos necesarios
            user.dni = request.POST.get('dni')
            user.username = request.POST.get('nom_user')
            user.ape_pat = request.POST.get('ape_pat')
            user.ape_mat = request.POST.get('ape_mat')
            user.genero = request.POST.get('genero')
            user.contacto = request.POST.get('contacto')
            user.direccion = request.POST.get('direccion')
            user.email = request.POST.get('email')

            # Obtener la instancia de Ciudad correspondiente
            ciudad_id = request.POST.get('id_ciudad')
            ciudad = Ciudad.objects.get(id_ciudad=ciudad_id)
            user.id_ciudad = ciudad

            # Guardar los cambios en la base de datos
            user.save()

            return redirect('listarCliente')
        else:
            return HttpResponse("Faltan datos en el formulario")
    else:
        users = Cliente.objects.all()
        datos = {'cliente': users}
        return render(request, "Cliente/actualizarCliente.html", datos)


def agregarCliente(request):
    if request.method == 'POST':
        dni = request.POST.get('dni')
        username = request.POST.get('username')
        ape_pat = request.POST.get('ape_pat')
        ape_mat = request.POST.get('ape_mat')
        genero = request.POST.get('genero')
        contacto = request.POST.get('contacto')
        direccion = request.POST.get('direccion')
        email = request.POST.get('email')
        id_ciudad = request.POST.get('id_ciudad')

        # Imprime los valores de los campos para depurar
        print(dni, username, ape_pat, ape_mat, genero,
              contacto, direccion, email, id_ciudad)

        if dni and username and ape_pat and ape_mat and genero and contacto and direccion and email and id_ciudad:
            # Obtener la instancia de la ciudad
            ciudad = get_object_or_404(Ciudad, id_ciudad=id_ciudad)
            user = Cliente()
            user.dni = dni
            user.username = username
            user.ape_pat = ape_pat
            user.ape_mat = ape_mat
            user.genero = genero
            user.contacto = contacto
            user.direccion = direccion
            user.email = email
            user.id_ciudad = ciudad  # Asignar la instancia de la ciudad en lugar del ID
            user.save()
            return redirect('agregarCliente')
        else:
            return HttpResponse("Faltan datos en el formulario")
    else:
        return render(request, "registro_cliente.html")


def eliminarCliente(request):
    if request.method == 'POST':
        if request.POST.get('id_cliente'):
            id_a_borrar = request.POST.get('id_cliente')
            try:
                usuario = Cliente.objects.get(id_cliente=id_a_borrar)
                usuario.delete()
                return redirect('listarCliente')
            except Cliente.DoesNotExist:
                return redirect('listarCliente')
    else:
        users = Cliente.objects.all()
        datos = {'cliente': users}
        return render(request, "Cliente/eliminarCliente.html", datos)


def listarCliente(request):
    users = Cliente.objects.all()
    datos = {'cliente': users}
    return render(request, "Cliente/listarCliente.html", datos)


################## Reserva ################

def actualizarReserva(request):
    if request.method == "POST":
        if (
            request.POST.get('id_reserva')
            and request.POST.get('cant_nino')
            and request.POST.get('cant_adulto')
            and request.POST.get('tot_cant')
            and request.POST.get('id_pasaj')
            and request.POST.get('id_tour')
        ):
            # Obtener el objeto de usuario a actualizar
            user = Reserva.objects.get(
                id_cliente=request.POST.get('id_reserva'))

            # Actualizar los campos necesarios

            user.cant_nino = request.POST.get('cant_niño')
            user.cant_adulto = request.POST.get('cant_adulto')
            user.tot_cant = request.POST.get('tot_cant')
            user.id_pasaj = request.POST.get('id_pasaj')
            user.id_tour = request.POST.get('id_tour')

            # Guardar los cambios en la base de datos
            user.save()

            return redirect('listarReserva')
    else:
        users = Reserva.objects.all()
        datos = {'reserva': users}
        return render(request, "Reserva/actualizarReserva.html", datos)


def agregarReserva(request):
    if request.method == 'POST':
        cant_niño = request.POST.get('cant_niño')
        cant_adulto = request.POST.get('cant_adulto')
        tot_cant = request.POST.get('tot_cant')
        id_pasaj = request.POST.get('email')
        id_tour = request.POST.get('id_ciudad')

        # Imprime los valores de los campos para depurar
        print(cant_niño, cant_adulto, tot_cant, id_pasaj, id_tour)

        if cant_niño and cant_adulto and tot_cant and id_pasaj and id_tour:
            user = Reserva()
            user.cant_nino = cant_niño
            user.cant_adulto = cant_adulto
            user.tot_cant = tot_cant
            user.id_pasaj = id_pasaj
            user.id_tour = id_tour
            user.save()
            return redirect('listarReserva')
        else:
            return HttpResponse("Faltan datos en el formulario")
    else:
        return render(request, "Reserva/agregarReserva.html")


def eliminarReserva(request):
    if request.method == 'POST':
        if request.POST.get('id_reserva'):
            id_a_borrar = request.POST.get('id_reserva')
            try:
                usuario = Reserva.objects.get(id_reserva=id_a_borrar)
                usuario.delete()
                return redirect('listarReserva')
            except Reserva.DoesNotExist:
                return redirect('listarReserva')
    else:
        users = Reserva.objects.all()
        datos = {'reserva': users}
        return render(request, "Reserva/eliminarReserva.html", datos)


def listarReserva(request):
    users = Reserva.objects.all()
    datos = {'reversa': users}
    return render(request, "Reserva/listarReserva.html", datos)


################## Tour ################

def actualizarTour(request):
    if request.method == "POST":
        if (
            request.POST.get('id_tour')
            and request.POST.get('nom_tour')
            and request.POST.get('fecha_tour')
            and request.POST.get('desc_tour')
            and request.POST.get('valor_tour')
        ):
            # Obtener el objeto de usuario a actualizar
            user = Tour.objects.get(
                id_tour=request.POST.get('id_tour'))

            # Actualizar los campos necesarios
            user.nom_tour = request.POST.get('nom_tour')
            user.fecha_tour = request.POST.get('fecha_tour')
            user.desc_tour = request.POST.get('desc_tour')
            user.valor_tour = request.POST.get('valor_tour')

            # Guardar los cambios en la base de datos
            user.save()

            return redirect('listarTour')
    else:
        users = Tour.objects.all()
        datos = {'tour': users}
        return render(request, "Tour/actualizarTour.html", datos)


def agregarTour(request):
    if request.method == 'POST':
        nom_tour = request.POST.get('nom_tour')
        fecha_tour = request.POST.get('fecha_tour')
        desc_tour = request.POST.get('desc_tour')
        valor_tour = request.POST.get('valor_tour')

        # Imprime los valores de los campos para depurar
        print(nom_tour, fecha_tour, desc_tour, valor_tour)

        if nom_tour and fecha_tour and desc_tour and valor_tour:
            user = Tour()
            user.nom_tour = nom_tour
            user.fecha_tour = fecha_tour
            user.desc_tour = desc_tour
            user.valor_tour = valor_tour

            user.save()
            return redirect('listarTour')
        else:
            return HttpResponse("Faltan datos en el formulario")
    else:
        return render(request, "Tour/agregarTour.html")


def eliminarTour(request):
    if request.method == 'POST':
        if request.POST.get('id_tour'):
            id_a_borrar = request.POST.get('id_tour')
            try:
                usuario = Tour.objects.get(id_tour=id_a_borrar)
                usuario.delete()
                return redirect('listarTour')
            except Cliente.DoesNotExist:
                return redirect('listarTour')
    else:
        users = Tour.objects.all()
        datos = {'tour': users}
        return render(request, "Tour/eliminarTour.html", datos)


def listarTour(request):
    users = Tour.objects.all()
    datos = {'tour': users}
    return render(request, "Tour/listarTour.html", datos)


############### Contacto###########
def listarContacto(request):
    users = Contacto.objects.all()
    datos = {'contacto': users}
    return render(request, "Contacto/listarContacto.html", datos)


def agregarContacto(request):
    if request.method == 'POST':
        nom_contacto = request.POST.get('nom_contacto')
        ape_contacto = request.POST.get('ape_contacto')
        email_contacto = request.POST.get('email_contacto')
        fono_contacto = request.POST.get('fono_contacto')
        mensaje = request.POST.get('mensaje')
        # Imprime los valores de los campos para depurar
        print(nom_contacto, ape_contacto, email_contacto, fono_contacto)

        if nom_contacto and ape_contacto and email_contacto and fono_contacto:
            user = Contacto()
            user.nom_contacto = nom_contacto
            user.ape_contacto = ape_contacto
            user.email_contacto = email_contacto
            user.fono_contacto = fono_contacto
            user.mensaje = mensaje

            user.save()
            return redirect('contacto')
        else:
            return HttpResponse("Faltan datos en el formulario")
    else:
        return render(request, "contacto.html")
