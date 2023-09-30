# Generated by Django 4.2.5 on 2023-09-29 04:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoClienteInstituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agencia', models.CharField(max_length=5)),
                ('conta', models.CharField(max_length=9)),
                ('senha', models.CharField(max_length=12)),
                ('saldo_bancario', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('saldo_drex', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('foto_instituicao', models.ImageField(null=True, upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Moedas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NavItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, null=True)),
                ('url', models.CharField(max_length=100, null=True)),
                ('icone', models.TextField(max_length=500, null=True)),
            ],
        ),
    ]
