from django.contrib import admin
from app.models import Servicio, Subscripcion, Cliente

class ServicioAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','tipoServicio','nombreEmpresa','direccion', 'contacto', 'correo']
    
admin.site.register(Servicio, ServicioAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','apellido','edad','servicio', 'correo','formapago']
admin.site.register(Cliente, ClienteAdmin)

class SubscripcionAdmin(admin.ModelAdmin):
    list_display = ['id','cliente','servicio','Subscripcion_type','created_at', 'precio','finish']
admin.site.register(Subscripcion, SubscripcionAdmin)

