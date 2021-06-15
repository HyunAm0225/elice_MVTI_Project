from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
app_name = 'character'

router.register('character', views.CharacterViewSet)


urlpatterns = [
    path('sentiment/', views.SentimentAnalyzeView.as_view(), name='sentiment'),
    path('', include(router.urls))
]
