from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class CustomModelViewSet(ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UsuarioCustomizadoView(ModelViewSet):
    queryset = UsuarioCustomizado.objects.all()
    serializer_class = UsuarioCustomizadoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = UsuarioCustomizado.objects.filter(id=user.id)        
        return queryset

class CategoriaLivrosView(ModelViewSet):
    queryset = CategoriaLivros.objects.all() #select *from CategoriaLivros
    serializer_class = CategoriaLivrosSerializer
    #permission_classes = (IsAuthenticated,)

class AutorView(ModelViewSet):
    queryset = Autor.objects.all() 
    serializer_class = AutorSerializer

class LivrosView(ModelViewSet):
    queryset = Livros.objects.all() 
    serializer_class = LivrosSerializer

class EmprestimoView(ModelViewSet):
    queryset = Emprestimo.objects.all() 
    serializer_class = EmprestimoSerializer

class EmprestimoLivrosView(CustomModelViewSet):
    queryset = EmprestimoLivros.objects.all() 
    serializer_class = EmprestimoLivrosSerializer