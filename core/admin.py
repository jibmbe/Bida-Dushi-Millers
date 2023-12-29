from django.contrib import admin
from .models import Invoice, Service
from .forms import InvoiceAdminForm

class InvoiceAdmin(admin.ModelAdmin):
    form = InvoiceAdminForm

admin.site.register(Service)
admin.site.register(Invoice,InvoiceAdmin,)

