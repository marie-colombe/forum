from api.models.message_model import MessageModel
from api.serializers.message_serializer import MessageSerializer
from rest_framework import viewsets


    


class MessageViewset(viewsets.ModelViewSet):
    serializer_class =  MessageSerializer
    queryset = MessageModel.objects.all()