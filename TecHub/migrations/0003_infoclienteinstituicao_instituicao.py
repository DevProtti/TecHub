# Generated by Django 4.2.5 on 2023-09-29 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TecHub', '0002_informacaoclienteopenfinance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoclienteinstituicao',
            name='Instituicao',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='TecHub.instituicao'),
            preserve_default=False,
        ),
    ]
