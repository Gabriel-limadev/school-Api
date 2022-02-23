from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula
from .validators import *


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
    
    # Validações
    def validate(self, data):
        """Valida dados de alunos"""
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': 'O campo nome não pode conter números'})
    
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': 'O campo rg deve ter 9 digitos'})

        if not cpf_caracteres_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'O campo CPF deve ter 11 digitos'})
        elif not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'CPF digitado não existe'})
        
        if not data_valida(data['data_nascimento']):
            raise serializers.ValidationError({'data_nascimento': 'Data inválida'})
        
        return data
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

    # Validações
    def validate(self, data):
        """Valida dados de alunos"""
        if not codigo_valido(data['codigo_curso']):
            raise serializers.ValidationError({'codigo_curso': 'O campo código deve ter 5 digitos'})
        
        return data
           
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'
  
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
