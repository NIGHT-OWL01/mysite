from django.contrib import admin
from storage.models import ContactRelation,Contact
# Register your models here.

@admin.register(ContactRelation)
class ContactRelationAdmin(admin.ModelAdmin):
    list_display = ['id','relation_type']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','number','relation']