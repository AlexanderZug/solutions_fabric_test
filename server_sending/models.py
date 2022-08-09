from django.core.validators import RegexValidator
from django.db import models
import pytz

class StatusChoices(models.TextChoices):
    SEND = 'S', 'Send'
    NO_SEND = 'N', 'No send'


class Sending(models.Model):
    start = models.DateTimeField()
    stop = models.DateTimeField()
    massage = models.TextField()
    tag = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='tags', blank=True,
                            null=True)
    code = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='codes',
                             blank=True, null=True)


class Client(models.Model):
    regex = RegexValidator(regex=r'^7\d{10}$')
    tel_number = models.CharField(validators=[regex], unique=True, max_length=11, default='7')
    mobile_code = models.CharField(max_length=4)
    tag = models.CharField(max_length=20)
    time_zone = models.CharField(max_length=50, choices=[(timezone, timezone) for timezone in pytz.common_timezones], default='UTC')

    def __str__(self):
        return f'{self.tag}, {self.mobile_code}'


class Massage(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    sending = models.ForeignKey('Sending', on_delete=models.CASCADE, related_name='sendings')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='clients')
    status = models.CharField(max_length=1, choices=StatusChoices.choices,
                              default=StatusChoices.NO_SEND)