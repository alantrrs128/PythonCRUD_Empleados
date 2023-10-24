"""
URL configuration for Tienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from empleados.views import EmpleadosListado, EmpleadosDetalle, EmpleadosCrear, EmpleadosActualizar, EmpleadosEliminar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empleados/', EmpleadosListado.as_view(template_name = "empleados/index.html"), name = 'leer'),
    path('empleados/detalles/<int:pk>', EmpleadosDetalle.as_view(template_name = "empleados/detalles.html"), name = 'detalles'),
    path('empleados/crear', EmpleadosCrear.as_view(template_name = "empleados/crear.html"), name = 'crear'),
    path('empleados/editar/<int:pk>', EmpleadosActualizar.as_view(template_name = "empleados/actualizar.html"), name = 'actualizar'),
    path('empleados/eliminar/<int:pk>', EmpleadosEliminar.as_view(), name = 'eliminar'),
]
