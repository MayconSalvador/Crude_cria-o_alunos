from django.urls import path
from . import views
#from .views import exportar_excel

urlpatterns = [
    path('criar_alunos/', views.criar_alunos, name='criar_alunos'),
    path('deletar_aluno/<int:id>/', views.deletar_aluno, name='deletar_aluno'),
    path('exportar-excel/', views.exportar_excel, name='exportar_excel'),
]