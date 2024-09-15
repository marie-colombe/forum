from api.models.subject_model import SubjectModel
from api.serializers.subject_serializer import SubjectSerializer
from rest_framework import viewsets


    


class SubjectViewset(viewsets.ModelViewSet):
    serializer_class =  SubjectSerializer
    queryset = SubjectModel.objects.all()