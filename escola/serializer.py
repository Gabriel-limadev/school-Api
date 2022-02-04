from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        
class MatriculaSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source='aluno.nome')  
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        exclude = []
        
    def get_periodo(self, obj):
        return obj.get_periodo_display()
        
class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    # Deixando os campos com uma melhor visualização. 
    # Ex: Ao inves do id 1 veremos Curso Python
    curso = serializers.ReadOnlyField(source='curso.descricao')
    # Ex: Ao inves de N veremos Noturno
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    
    # Method do SerializerMethodField()
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaAlunosMatriculaSerializer(serializers.ModelSerializer):
    # Deixando os campos com uma melhor visualização. 
    # Ex: Ao inves do id 1 veremos Gabriel Lima
    aluno = serializers.ReadOnlyField(source='aluno.nome')      
    class Meta:
        model = Matricula
        fields = ['aluno']
