from django.urls import path 

# importando tudo das views
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'character', CharacterAPIView)
router.register(r'location', LocationAPIView)
router.register(r'episode', EpisodeAPIView)

urlpatterns = router.urls
