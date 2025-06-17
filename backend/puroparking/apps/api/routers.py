from rest_framework.routers import DefaultRouter
from ..rol.views import *
from ..facturacion.views import *

router = DefaultRouter()

router.register(r'facturacion', facturacionViewset, basename='facturacion')
router.register(r'hora_parqueo', hora_parqueoViewset, basename='hora_parqueo')
router.register(r'rol', rolViewset, basename='rol')
router.register(r'servicio', servicioViewset, basename='servicio')
router.register(r'servicio', servicioViewset, basename='usuario')
router.register(r'vehiculo', vehiculoViewset, basename='vehiculo')

urlpatterns = router.urls