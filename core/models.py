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

class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    nome_do_autor = models.CharField(max_length=200)
    assunto = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=50)
    ano_da_publicacao = models.DateField()

    def __str__(self):
        return self.titulo


class Autor(models.Model):
    class Meta:
        verbose_name_plural = 'autores'

    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)

    def __str__(self):
        return self.sobrenome.upper()+', ' + self.nome


class Aluno(models.Model):
    matricula = models.CharField(max_length=12, unique=True)
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    ano_publicacao = models.IntegerField()

    def __str__(self):
        return '{}, ({})'.format(self.titulo, self.ano_publicacao)


class Emprestimo(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_retirada = models.DateField()
    data_devolucao = models.DateField()
    livros = models.ManyToManyField(Livro)
    devolvido = models.BooleanField()


