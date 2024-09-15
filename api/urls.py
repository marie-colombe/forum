from django.urls import path, include
from rest_framework import routers
from api.api_viewsets.forum_api_viewset import ForumViewset
from api.api_viewsets.message_api_viewset import MessageViewset
from api.api_viewsets.subject_api_viewset import SubjectViewset


router = routers.DefaultRouter()

router.register(r'forum', ForumViewset)
router.register(r'message', MessageViewset)
router.register(r'subject', SubjectViewset)



urlpatterns = [   

    path('forum',include(router.urls)),
    path('message',include(router.urls)),
    path('subject',include(router.urls)),
  ] 