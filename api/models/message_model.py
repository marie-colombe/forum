from django.db import models
from api.models.subject_model import SubjectModel
from base.models.helpers.date_time_model import DateTimeModel




class MessageModel(DateTimeModel):
     contenu = models.TextField()
     auteur = models.CharField(max_length=255)
     date_post = models.DateField(auto_now_add=True)
     sujet = models.ForeignKey('api.SubjectModel', on_delete=models.CASCADE, related_name='messages')



     def _str_(self):
        return f'{self.auteur} - {self.date_post}'







 
    



     

    


   





   

# 





# # La table  message

# class Message(models.Model):
   

#     def _str_(self):
#         return f'{self.auteur} - {self.date_post}'
