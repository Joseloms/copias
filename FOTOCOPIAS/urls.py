# encoding:utf-8

"""FOTOCOPIAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from apps.copias.views import NivelCreate, NivelList, NivelDetail, NivelUpdate, NivelDelete, DocenteList, DocenteCreate, \
    DocenteDelete, DocenteDetail, DocenteUpdate, CopiaCreate, CopiaDelete, CopiaDetail, CopiaList, CopiaUpdate, \
    DocenteBuscadorList, DocenteBuscadorCopiaList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nivel/', NivelList.as_view(template_name="nivel/index.html"), name='nivel_lista'),
    path('nivel/detalle/<int:pk>', NivelDetail.as_view(template_name="nivel/detalles.html"), name='nivel_detalles'),
    path('nivel/crear', NivelCreate.as_view(template_name="nivel/crear.html"), name='nivel_crear'),
    path('nivel/editar/<int:pk>', NivelUpdate.as_view(template_name="nivel/actualizar.html"),
         name='nivel_actualizar'),
    path('nivel/eliminar/<int:pk>', NivelDelete.as_view(), name='nivel_eliminar'),

    path('docente/', DocenteList.as_view(template_name="docente/index.html"), name='docente_lista'),
    path('docente/detalle/<int:pk>', DocenteDetail.as_view(template_name="docente/detalles.html"),
         name='docente_detalles'),
    path('docente/crear', DocenteCreate.as_view(template_name="docente/crear.html"), name='docente_crear'),
    path('docente/editar/<int:pk>', DocenteUpdate.as_view(template_name="docente/actualizar.html"),
         name='docente_actualizar'),
    path('docente/eliminar/<int:pk>', DocenteDelete.as_view(), name='docente_eliminar'),
    path('docente/buscador', DocenteBuscadorList.as_view(template_name="docente/index.html"), name='docente_buscador'),

    path('copia/', CopiaList.as_view(template_name="copia/index.html"), name='copia_lista'),
    path('copia/detalle/<int:pk>', CopiaDetail.as_view(template_name="copia/detalles.html"),
         name='copia_detalles'),
    path('copia/crear', CopiaCreate.as_view(template_name="copia/crear.html"), name='copia_crear'),
    path('copia/editar/<int:pk>', CopiaUpdate.as_view(template_name="copia/actualizar.html"),
         name='copia_actualizar'),
    path('copia/eliminar/<int:pk>', CopiaDelete.as_view(), name='copia_eliminar'),
    path('copia/buscador', DocenteBuscadorCopiaList.as_view(template_name="copia/index.html"), name='copia_docente_buscador'),

]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
