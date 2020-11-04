# Generated by Django 3.1.3 on 2020-11-04 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201104_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colheita',
            name='arvore',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arvore', to='api.arvores'),
        ),
        migrations.AlterField(
            model_name='colheita',
            name='grupo_arvores',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grupo_arvores', to='api.grupoarvores'),
        ),
    ]