from django.urls import path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from mociAPIC.views import encuestaViewSet, usuarioViewSet

router = DefaultRouter()
router.register(r'encuesta', encuestaViewSet)
router.register(r'usuario', usuarioViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin', admin.site.urls),
    
    
    
]