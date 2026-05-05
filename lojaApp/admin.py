from django.contrib import admin
from .models import sorvete, comentario, categoria, fornecedor, opcaoDietica

admin.site.register(sorvete)
admin.site.register(comentario)
admin.site.register(categoria)
admin.site.register(fornecedor)
admin.site.register(opcaoDietica)