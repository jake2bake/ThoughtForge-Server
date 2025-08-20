from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from thoughtsapi.views.users import profile_view
from thoughtsapi.views import *
from thoughtsapi.views import gutendex_proxy



router = routers.DefaultRouter(trailing_slash=False)
router.register(r"entries", Entries, "entry")
router.register(r"topics", TopicViewSet, "topic")
router.register(r'tags', TagViewSet, 'tag')
router.register(r'entryTags', EntryTagViewSet, 'entryTags')
router.register(r"readings", ReadingViewSet, 'reading')
router.register(r"readingAssignments", ReadingAssignmentViewSet, 'readingAssignment')
router.register(r"courses", CourseViewSet, 'course')
router.register(r"courseEnrollments", CourseEnrollmentViewSet, 'courseEnrollment')
router.register(r"submissions", SubmissionViewSet, 'submission')
router.register(r"likes", LikeViewSet, 'like')
router.register(r'shares', ShareViewSet, 'share')
router.register(r"users", UserViewSet, 'user')



urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login', login_user, name='login'),
    path("profile/", profile_view, name='profile'),
    path('gutendex/books/<int:gutenberg_id>/', gutendex_proxy, name='gutendex-proxy'),
    path('gutendex/books', gutendex_search, name='gutendex-search'),
    path('gutendex/text/', gutendex_text_proxy, name='gutendex-text-proxy')
]
