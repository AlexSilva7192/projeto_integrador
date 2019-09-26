from django.db import models

# Create your models here.

from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    nome_do_autor = models.CharField(max_length=200)
    assunto = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=50)
    ano_da_publicacao = models.DateField()

    def __str__(self):
        return self.titulo

