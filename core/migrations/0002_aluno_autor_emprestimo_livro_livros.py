# Generated by Django 2.2.5 on 2019-09-30 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=12, unique=True)),
                ('nome', models.CharField(max_length=50)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'autores',
            },
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('nome_do_autor', models.CharField(max_length=200)),
                ('assunto', models.CharField(max_length=100)),
                ('editora', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=50)),
                ('ano_da_publicacao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('ano_publicacao', models.IntegerField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Autor')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_retirada', models.DateField()),
                ('data_devolucao', models.DateField()),
                ('devolvido', models.BooleanField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Aluno')),
                ('livros', models.ManyToManyField(to='core.Livro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]