import pytz
from django.core.validators import RegexValidator
from django.db import models


class StatusChoices(models.TextChoices):
    SEND = 'Send', 'Send'
    NO_SEND = 'No send', 'No send'


class Sending(models.Model):
    start = models.DateTimeField()
    stop = models.DateTimeField()
    massage_txt = models.TextField()
    tag = models.CharField(max_length=20, blank=True, null=True)
    code = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Client(models.Model):
    regex = RegexValidator(regex=r'^7\d{10}$')
    tel_number = models.CharField(
        validators=[regex], unique=True, max_length=11, default='7'
    )
    mobile_code = models.CharField(max_length=4)
    tag = models.CharField(max_length=20)
    time_zone = models.CharField(
        max_length=50,
        choices=[(timezone, timezone) for timezone in pytz.common_timezones],
        default='UTC',
    )

    def __str__(self):
        return self.tel_number


class Massage(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    sending = models.ForeignKey(
        'Sending', on_delete=models.CASCADE, related_name='sendings'
    )
    client = models.ForeignKey(
        'Client', on_delete=models.CASCADE, related_name='clients'
    )
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.NO_SEND,
    )

    def __str__(self):
        return str(self.id)
