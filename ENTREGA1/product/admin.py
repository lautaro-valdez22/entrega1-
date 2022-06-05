from django.contrib import admin

from product.models import Celulares, Heladeras, Televisores

# Register your models here.
admin.site.register(Celulares)
admin.site.register(Heladeras)
admin.site.register(Televisores)