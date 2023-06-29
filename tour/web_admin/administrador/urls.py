
from django.contrib import admin
from django.urls import path

from django import views  # <<==========
from . import views  # <<==========


urlpatterns = [


    # URLs de web_admin en administrador
    # path('', views.index),  # <<==========
    path('', views.index, name='index'),
    ####### ELIMINAR USUARIO##############################
    path('agregar', views.agregar, name="agregar"),
    path('actualizar', views.actualizar, name="actualizar"),
    path('listar', views.listar, name="listar"),
    path('eliminar', views.eliminar, name="eliminar"),

    ###########################################################

    path('agregarGuia', views.agregarGuia, name="agregarGuia"),
    path('actualizarGuia', views.actualizarGuia, name="actualizarGuia"),
    path('listarGuia', views.listarGuia, name="listarGuia"),
    path('eliminarGuia', views.eliminarGuia, name="eliminarGuia"),

    ###########################################################

    path('agregarFactura', views.agregarFactura, name="agregarFactura"),
    path('actualizarFactura', views.actualizarFactura, name="actualizarFactura"),
    path('listarFactura', views.listarFactura, name="listarFactura"),
    path('eliminarFactura', views.eliminarFactura, name="eliminarFactura"),

    ###########################################################

    path('agregarCliente', views.agregarCliente, name="agregarCliente"),
    path('actualizarCliente', views.actualizarCliente, name="actualizarCliente"),
    path('listarCliente', views.listarCliente, name="listarCliente"),
    path('eliminarCliente', views.eliminarCliente, name="eliminarCliente"),

    ###########################################################

    path('agregarReserva', views.agregarReserva, name="agregarReserva"),
    path('actualizarReserva', views.actualizarReserva, name="actualizarReserva"),
    path('listarReserva', views.listarReserva, name="listarReserva"),
    path('eliminarReserva', views.eliminarReserva, name="eliminarReserva"),


    ###########################################################

    path('agregarTour', views.agregarTour, name="agregarReserva"),
    path('actualizarTour', views.actualizarTour, name="actualizarTour"),
    path('listarTour', views.listarTour, name="listarTour"),
    path('eliminarTour', views.eliminarTour, name="eliminarTour"),

    ###########################################################
    path('listarContacto', views.listarContacto, name="listarContacto"),
    path('agregarContacto', views.agregarContacto, name="agregarContacto"),

]
