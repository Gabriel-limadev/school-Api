from rest_framework import viewsets, generics, filters
from .models import Student, Course, Registration
from .serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationStudentSerializer, ListStudentRegistrationSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentsViewSet(viewsets.ModelViewSet):
    """Showing all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # Filters
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', 'date_birth']
    search_fields = ['nome']
    # Authentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class CoursesViewSet(viewsets.ModelViewSet):
    """Showing all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # Filters
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['course_code', 'level']
    search_fields = ['course_code']
    # Authentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class RegistrationsViewSet(viewsets.ModelViewSet):
    """Showing all courses registrations"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    # Filters
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['student']
    search_fields = ['student__name', 'course__description']
    # Authentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListRegistrationsStudent(generics.ListAPIView):
    """Listing all student enrollments"""
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationStudentSerializer
    # Filters
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['course']
    search_fields = ['course__description']
    # Authentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListStudentsRegistration(generics.ListAPIView):
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListStudentRegistrationSerializer
    # Filters
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['student']
    search_fields = ['student__name']
    # Authentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated ]
    