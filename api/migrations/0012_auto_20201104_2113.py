# Generated by Django 3.1.3 on 2020-11-05 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20201104_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colheita',
            name='grupo_arvores',
        ),
        migrations.AddField(
            model_name='colheita',
            name='grupo_arvores',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.grupoarvores', verbose_name='Grupo de Árvores'),
        ),
    ]
