from django.contrib import admin
from django.urls import path, include
from scholl.views import StudentsViewSet, CoursesViewSet, RegistrationsViewSet, ListRegistrationsStudent, ListStudentsRegistration
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Sourses')
router.register('registrations', RegistrationsViewSet, basename='Registrations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/registration/', ListRegistrationsStudent.as_view()),
    path('courses/<int:pk>/registration/', ListStudentsRegistration.as_view())
]
