from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from thoughtsapi.views import *



router = routers.DefaultRouter(trailing_slash=False)
router.register(r"entries", Entries, "entry")
router.register(r"topics", TopicViewSet, "topic")
router.register(r'tags', TagViewSet, 'tag')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login', login_user, name='login')
]

