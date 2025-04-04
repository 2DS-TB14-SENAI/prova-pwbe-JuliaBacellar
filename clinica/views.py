from django.shortcuts import render ,redirect
from .models import Medico , Consulta
from rest_framework.response import Response 
from .serializers import MedicoSerializer, ConsultaSerializer
from rest_framework import status 
from rest_framework.decorators import api_view 
from .forms import Medico
from django import template
# Create your views here.
### Views obrigatórias:
# 1. `listar_medicos` - Lista todos os médicos cadastrados
# 2. `criar_consulta` - Formulário para agendar nova consulta
# 3. `detalhes_consulta` - Exibe informações de uma consulta específica

@api_view(['GET'])
def listar_medicos(request):
    if request.method == 'GET':
        medicos = Medico.objects.all()
        serializer = MedicoSerializer(medicos, many=True)
        return Response(serializer.data)
    
@api_view(['POST']) 
def criar_consulta(request): 
    if request.method == 'POST':
        serializer = ConsultaSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])        
def detalhes_consulta(request, id ):
   if request.method =='GET': 
        try:
            detalhes_consulta = Consulta.objects.get(id=id)
        except Consulta.DoesNotExist:
            return Response(
                f"Error: {status.HTTP_404_NOT_FOUND} NOT FOUND",
                status=status.HTTP_404_NOT_FOUND
                )
        
        serializer = ConsultaSerializer(detalhes_consulta)
        return Response(serializer.data, status=status.HTTP_200_OK)
##o medico se cria pelo id dele

def medico(request):
    medico = medico.objects.all()

    if request.method == "POST":
        form = Medico(request.POST)
        if form.is_valid():
            form.save()##redireciona após salvar
            return redirect('medico:listar_medicos')
    else:
        form = Medico()

    return render(request, 'templates/listar_medicos.html', {'medico': medico, 'form': form})