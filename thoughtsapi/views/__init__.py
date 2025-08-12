from thoughtsapi.views.users import UserSerializer
from thoughtsapi.views.register import RegisterView
from thoughtsapi.views.login import login_user
from thoughtsapi.views.entries import Entries
from thoughtsapi.views.topics import TopicViewSet
from thoughtsapi.views.tags import TagViewSet
from thoughtsapi.views.entryTags import EntryTagViewSet
from thoughtsapi.views.readings import ReadingViewSet
from thoughtsapi.views.readingAssignments import ReadingAssignmentViewSet
from thoughtsapi.views.courses import CourseViewSet
from thoughtsapi.views.courseEnrollments import CourseEnrollmentViewSet
from thoughtsapi.views.submissions import SubmissionViewSet
from thoughtsapi.views.likes import LikeViewSet
from thoughtsapi.views.shares import ShareViewSet
from thoughtsapi.views.gutendex import gutendex_proxy, gutendex_search