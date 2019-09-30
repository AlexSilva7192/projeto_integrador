from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import *

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')

class LivrosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'nome_do_autor', 'assunto')

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'data_nascimento')

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('data_devolucao', 'data_retirada', 'aluno', 'devolvido')
    filter_horizontal = ['livros']

admin.site.register(Livros, LivrosAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
