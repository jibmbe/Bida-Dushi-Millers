from django.contrib import admin
from .models import Invoice, Service
from .forms import InvoiceAdminForm
from .models import UserMessage


class InvoiceAdmin(admin.ModelAdmin):
    form = InvoiceAdminForm

class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp')
    search_fields = ('user__username', 'message')


admin.site.register(Service)
admin.site.register(Invoice,InvoiceAdmin,)
admin.site.register(UserMessage, UserMessageAdmin)
