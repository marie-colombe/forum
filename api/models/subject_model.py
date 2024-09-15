from django.db import models
from api.models.forum_model import ForumModel 
from base.models.helpers.date_time_model import DateTimeModel




class SubjectModel(DateTimeModel):
    titre = models.CharField(max_length=255)
    date_creation = models.DateField(auto_now_add=True)
    forum = models.ForeignKey('api.ForumModel', on_delete=models.CASCADE, related_name='sujets')



     
    def _str_(self):
        return f"{self.nom}" 


     

   





   


