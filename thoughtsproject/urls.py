from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from thoughtsapi.views.users import profile_view
from thoughtsapi.views import *



router = routers.DefaultRouter(trailing_slash=False)
router.register(r"entries", Entries, "entry")
router.register(r"topics", TopicViewSet, "topic")
router.register(r'tags', TagViewSet, 'tag')
router.register(r"readings", ReadingViewSet, 'reading')
router.register(r"readingAssignments", ReadingAssignmentViewSet, 'readingAssignment')
router.register(r"courses", CourseViewSet, 'course')
router.register(r"courseEnrollments", CourseEnrollmentViewSet, 'courseEnrollment')
router.register(r"submissions", SubmissionViewSet, 'submission')
router.register(r"likes", LikeViewSet, 'like')
router.register(r'shares', ShareViewSet, 'share')



urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login', login_user, name='login'),
    path("profile/", profile_view, name='profile')
]
