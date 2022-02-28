from rest_framework import serializers
from school.models import Student, Course, Registration
from .validators import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    
    # Validations
    def validate(self, data):
        """Validate studant data """

        if not valid_name(data['name']):
            raise serializers.ValidationError({'name': 'The name field cannot contain numbers'})
    
        if not valid_rg(data['rg']):
            raise serializers.ValidationError({'rg': 'The name field must have 9 digits'})

        if not valid_cpf_characters(data['cpf']):
            raise serializers.ValidationError({'cpf': 'The name field must have 11 digits'})
        elif not valid_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf': 'CPF entered does not exist'})
        
        if not valid_date(data['date_birth']):
            raise serializers.ValidationError({'date_birth': 'Invalid data: The date of birth cannot be that year'})
        
        return data
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    # Validations
    def validate(self, data):
        """Validate course data"""
        if not valid_code(data['course_code']):
            raise serializers.ValidationError({'course_code': 'The name field must have 5 digits'})
        
        return data
           
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
  
class ListRegistrationStudentSerializer(serializers.ModelSerializer):
    # Leaving the fields with a better view
    # Ex: Instead of id 1, we will see Python Course
    course = serializers.ReadOnlyField(source='course.description')
    # Ex: Instead of N, we will see Nocturnal
    period = serializers.SerializerMethodField()
    class Meta:
        model = Registration
        fields = ['course', 'period']
    
    # Method of SerializerMethodField()
    def get_period(self, obj):
        return obj.get_period_display()
    
class ListStudentRegistrationSerializer(serializers.ModelSerializer):
    # Leaving the fields with a better view
    # Ex: Instead of id 1, we will see Gabriel Lima
    student = serializers.ReadOnlyField(source='student.name')      
    class Meta:
        model = Registration
        fields = ['student']
