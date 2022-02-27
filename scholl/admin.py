from django.contrib import admin
from scholl.models import Student, Course, Registration
# Register your models here.

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'date_birth')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'course_code', 'description')
    list_display_links = ('id', 'course_code')
    search_fields = ('course_code', )

admin.site.register(Course, Courses)

class Registrations(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('id', )
    
admin.site.register(Registration, Registrations)