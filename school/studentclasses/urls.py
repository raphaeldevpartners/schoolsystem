from rest_framework import routers
from django.conf.urls import include, url
from studentclasses import views
# from studentclasses import views
router = routers.DefaultRouter()

router.register('students', views.StudentViewSet)
router.register('teachers', views.TeacherViewSet)
router.register('subjects', views.SubjectViewSet)
router.register('rooms', views.RoomViewSet)
router.register('schedules', views.ScheduleViewSet)
router.register('lectures', views.LectureViewSet)
router.register('studentlectures', views.StudentlectureViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^custom/get/$', views.CustomGet.as_view()),
]
