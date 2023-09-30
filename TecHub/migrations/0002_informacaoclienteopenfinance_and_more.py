# Generated by Django 4.2.5 on 2023-09-29 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TecHub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformacaoClienteOpenFinance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_instituicao_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info_instituicao_user', to='TecHub.infoclienteinstituicao')),
                ('instituicao_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instituicao_user', to='TecHub.instituicao')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]