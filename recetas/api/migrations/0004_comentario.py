# Generated by Django 5.1.2 on 2024-10-24 21:08

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comentario', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('id_Receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.receta')),
                ('id_Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
    ]
