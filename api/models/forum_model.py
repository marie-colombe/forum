from django.db import models

from base.models.helpers.date_time_model import DateTimeModel




class ForumModel(DateTimeModel):

    nom = models.CharField(max_length=255)
    description = models.TextField()


    def _str_(self):
         return self.nom
   





   

