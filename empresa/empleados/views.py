from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Empleados

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

class EmpleadosListado(ListView):
    model = Empleados

class EmpleadosCrear(SuccessMessageMixin, CreateView):
    model = Empleados
    form = Empleados
    fields = "__all__"
    success_message = 'El empleado fue dado de alta correctamente'

    def get_success_url(self):
        return reverse('leer')

class EmpleadosDetalle(DetailView):
    model = Empleados

class EmpleadosActualizar(SuccessMessageMixin, UpdateView):
    model = Empleados
    form = Empleados
    fields = "__all__"
    success_message = 'El empleado fue actualizado correctamente'

    def get_success_url(self):
        return reverse('leer')
    
class EmpleadosEliminar(SuccessMessageMixin, DeleteView):
    model = Empleados
    form = Empleados
    fields = "__all__"

    def get_success_url(self):
        success_message = 'El empleado fue eliminado correctamente'
        messages.success(self.request, (success_message))
        return reverse('leer')