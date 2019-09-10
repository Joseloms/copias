import datetime

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse, request
from django.core import serializers

from .models import Nivel, Docente, Copia


# Create your views here.

class NivelList(ListView):
    model = Nivel
    paginate_by = 5


class NivelDetail(DetailView):
    model = Nivel


class NivelCreate(SuccessMessageMixin, CreateView):
    model = Nivel
    fields = "__all__"
    success_message = 'Nivel Creado Correctamente !'

    def get_success_url(self):
        return reverse('nivel_lista')


class NivelUpdate(SuccessMessageMixin, UpdateView):
    model = Nivel
    fields = "__all__"
    success_message = 'Nivel Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('nivel_lista')


class NivelDelete(SuccessMessageMixin, DeleteView):
    model = Nivel
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Nivel Eliminado Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('nivel_lista')


class DocenteBuscadorList(ListView):
    model = Docente
    paginate_by = 5

    def get_queryset(self):
        queryset = super(DocenteBuscadorList, self).get_queryset()
        q = self.request.GET.get("q")
        if q:
            return queryset.filter(name__icontains=q)


class DocenteList(ListView):
    model = Docente
    paginate_by = 5


class DocenteDetail(DetailView):
    model = Docente


class DocenteCreate(SuccessMessageMixin, CreateView):
    model = Docente
    fields = "__all__"
    success_message = 'Docente Creado Correctamente !'

    def get_success_url(self):
        return reverse('docente_lista')


class DocenteUpdate(SuccessMessageMixin, UpdateView):
    model = Docente
    fields = "__all__"
    success_message = 'Docente Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('docente_lista')


class DocenteDelete(SuccessMessageMixin, DeleteView):
    model = Docente
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Docente Eliminado Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('docente_lista')



class DocenteBuscadorCopiaList(ListView):
    model = Copia
    paginate_by = 5

    def get_queryset(self):
        queryset = super(DocenteBuscadorCopiaList, self).get_queryset()
        q = self.request.GET.get("q")
        if q:
            return queryset.filter(docente__name__icontains=q)



class CopiaList(ListView):
    model = Copia
    paginate_by = 5


class CopiaDetail(DetailView):
    model = Copia


class CopiaCreate(SuccessMessageMixin, CreateView):
    model = Copia
    fields = "__all__"
    success_message = 'Copia Registrada Correctamente !'

    def get_success_url(self):
        return reverse('copia_lista')


class CopiaUpdate(SuccessMessageMixin, UpdateView):
    model = Copia
    fields = "__all__"
    success_message = 'Copia Actualizada Correctamente !'

    def get_success_url(self):
        return reverse('copia_lista')


class CopiaDelete(SuccessMessageMixin, DeleteView):
    model = Copia
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Copia Eliminada Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('copia_lista')
