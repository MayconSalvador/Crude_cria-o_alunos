from django.shortcuts import render, redirect ,get_object_or_404
from .models import Alunos
from django.http import HttpResponse
import pandas as pd


def criar_alunos (request):
    if request.method == 'GET':
        alunos = Alunos.objects.all()
        return render(request, 'criar_alunos.html', {'alunos':alunos})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_matricula = request.POST.get('data_matricula')
        ativo = request.POST.get('ativo')
        plano_aula = request.POST.get('plano_aula')

        aluno = Alunos(
            nome = nome,
            email= email,
            telefone= telefone,
            data_matricula= data_matricula,
            ativo = ativo,
            plano_aula = plano_aula,
        )

        aluno.save()
        return redirect('criar_alunos')
    
def deletar_aluno(request, id):
    aluno = get_object_or_404(Alunos, id=id)
    aluno.delete()
    return redirect('criar_alunos')