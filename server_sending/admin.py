from django.contrib import admin

from server_sending.models import Client, Massage, Sending


class SendingAdmin(admin.ModelAdmin):
    list_display = (
        'start',
        'stop',
        'massage_txt',
        'tag',
        'code',
    )
    search_fields = ('id',)


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'tel_number',
        'mobile_code',
        'tag',
    )


class MassageAdmin(admin.ModelAdmin):
    list_display = (
        'pub_date',
        'sending',
        'client',
        'status',
    )


admin.site.register(Sending, SendingAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Massage, MassageAdmin)
