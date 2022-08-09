from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import (ClientSerializer, MassageSerializer,
                             SendingSerializer)
from server_sending.models import Client, Massage, Sending


class SendingViewSet(ModelViewSet):
    queryset = Sending.objects.all()
    serializer_class = SendingSerializer

    @action(detail=True, methods=['get'])
    def detail_info(self, request, pk=None):
        queryset = Massage.objects.filter(sending_id=pk).all()
        if not queryset:
            raise serializers.ValidationError(
                'В этой рассылке не было отправлено сообщений.'
            )
        serializer = MassageSerializer(queryset, many=True)
        return Response(serializer.data)


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MassageViewSet(ModelViewSet):
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer
