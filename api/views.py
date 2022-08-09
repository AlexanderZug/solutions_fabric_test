
from rest_framework.viewsets import ModelViewSet

from api.serializers import SendingSerializer, ClientSerializer, MassageSerializer
from server_sending.models import Sending, Client, Massage


class SendingViewSet(ModelViewSet):
    queryset = Sending.objects.all()
    serializer_class = SendingSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MassageViewSet(ModelViewSet):
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer
