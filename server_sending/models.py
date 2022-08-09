from django.core.validators import RegexValidator
from django.db import models


class StatusChoices(models.TextChoices):
    SEND = 'S', 'Send'
    NO_SEND = 'N', 'No send'


class Sending(models.Model):
    star = models.DateTimeField()
    stop = models.DateTimeField()
    massage = models.TextField()
    tag = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='tags')
    status = models.ForeignKey('Massage', on_delete=models.CASCADE, related_name='statuses')


class Client(models.Model):
    regex = RegexValidator(regex=r'^7\d{10}$')
    tel_number = models.IntegerField(validators=[regex])
    mobile_code = models.IntegerField()
    tag = models.CharField(max_length=20)


class Massage(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    sending = models.ForeignKey('Sending', on_delete=models.CASCADE, related_name='sendings')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='clients')
    status = models.CharField(max_length=1, choices=StatusChoices.choices,
                              default=StatusChoices.NO_SEND)
