from django.contrib import admin
from .models import QrCode
# Register your models here.

@admin.register(QrCode)
class QrCodeAdmin(admin.ModelAdmin):
    list_fields=['id','title']