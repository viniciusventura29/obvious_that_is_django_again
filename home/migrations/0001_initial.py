# Generated by Django 4.1 on 2022-08-10 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Categoria', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('ativo', models.CharField(choices=[('A', 'Ativa'), ('I', 'Inativo')], max_length=5)),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.categoria')),
            ],
        ),
    ]
