from django.contrib import admin

from server_sending.models import Sending, Client, Massage


class SendingAdmin(admin.ModelAdmin):
    list_display = ('start', 'stop',
                    'massage', 'tag', 'code',)
    search_fields = ('id',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('tel_number', 'mobile_code', 'tag',)


class MassageAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'sending', 'client', 'status',)


admin.site.register(Sending, SendingAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Massage, MassageAdmin)
