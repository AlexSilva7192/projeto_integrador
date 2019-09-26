from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')

admin.site.register(Contato, ContatoAdmin)


from .models import Livro

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'nome_do_autor', 'assunto')

admin.site.register(Livro, LivroAdmin)


