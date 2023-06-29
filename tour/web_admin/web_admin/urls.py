"""web_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include  # <<==========
from administrador import views  # <<==========


urlpatterns = [
    path('admin/', admin.site.urls),  # <<==========
    path('mantenedores/', include('administrador.urls')),  # <<==========
    path('reserva_tour/', views.reserva_tour, name='reserva_tour'),
    path('tours/', views.tours, name='tours'),
    path('home_index/',views.home_index, name='home_index'),
    path('contacto/', views.agregarContacto, name='contacto'),
    path('acerca_de/', views.acerca_de, name='post_list'),
    path('elements/', views.elements, name='elements'),
    path('registro_cliente/', views.agregarCliente, name='registro_cliente'),
    path('pago_tour/', views.pago_tour, name='pago_tour'),
    path('pago_final/', views.pago_final, name='pago_final'),




]
