from rest_framework import viewsets, generics
from .models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculaSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos(as)"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListaMatriculasAluno(generics.ListAPIView):
    """Listando todas as matriculas de um aluno(a)"""
    
    # passando o queryset e o serializer_class como em todas outras views 
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListaAlunosMatricula(generics.ListAPIView):
    """Listando todos alunos(a) de um curso"""
    
    # passando o queryset e o serializer_class como em todas outras views 
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated ]
    