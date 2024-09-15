from api.models.forum_model import ForumModel
from api.serializers.forum_serializer import ForumSerializer
from rest_framework import viewsets


    


class ForumViewset(viewsets.ModelViewSet):
    serializer_class = ForumSerializer
    queryset = ForumModel.objects.all()