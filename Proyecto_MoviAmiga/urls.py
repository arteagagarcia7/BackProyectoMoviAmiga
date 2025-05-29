"""
URL configuration for Proyecto_MoviAmiga project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

# importar de django las url path, include y de restframework routers, vistas
# en settings en installed apps ponerla app creada
# from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Portales.views import BusesViewset
from Portales.views import ParaderosViewset
from Portales.views import PortalesViewset
from Portales.views import Programas_RutasViewset
from Portales.views import Puntos_RecargasViewset
from Portales.views import Rutas_ParaderosViewset
from Portales.views import Rutas_PuntosRecargasViewset
from Portales.views import RutasViewset


# crear las rutas de cada vista
router = DefaultRouter()
router.register('buses', BusesViewset, 'view_buses')
router.register('paraderos', ParaderosViewset, 'view_paraderos')
router.register('portales', PortalesViewset, 'view_portales')
router.register('programas_rutas', Programas_RutasViewset,
                'view_programas_rutas')
router.register('puntos_recarga', Puntos_RecargasViewset,
                'view_puntos_recarga')
router.register('rutas_paraderos', Rutas_ParaderosViewset, 'rutas_paraderos')
router.register('rutas_puntosrecargas',
                Rutas_PuntosRecargasViewset, 'rutas_puntosrecargas')
router.register('rutas', RutasViewset, 'rutas')


# usar path y poner la ruta para que funcione
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
