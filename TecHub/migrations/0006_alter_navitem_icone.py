from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TecHub', '0005_alter_navitem_icone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navitem',
            name='icone',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
