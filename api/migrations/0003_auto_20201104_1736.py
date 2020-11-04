# Generated by Django 3.1.3 on 2020-11-04 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201104_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colheita',
            name='arvore',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.arvores'),
        ),
        migrations.AlterField(
            model_name='colheita',
            name='grupo_arvores',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.grupoarvores'),
        ),
    ]