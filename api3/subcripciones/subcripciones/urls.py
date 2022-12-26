"""subcripciones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('Servicio',views.ServicioViewSet)
router.register('Cliente',views.ClienteViewSet)
router.register('Subscripcion',views.SubscripcionViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Servicios/', views.Servicio_list),
    path('Servicios/<int:pk>', views.Servicio_crud),
    path('Clientes/', views.Cliente_list),
    path('Clientes/<int:pk>', views.Cliente_crud),
    path('Subscripcions/', views.Subscripcion_list),
    path('Subscripcions/<int:pk>', views.Subscripcion_crud),
    path('', include(router.urls))
]
