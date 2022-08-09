from rest_framework import serializers

from server_sending.models import Sending, Client, Massage


class SendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sending
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class MassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Massage
        fields = '__all__'