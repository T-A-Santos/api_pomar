from django.db import models
from django.contrib import admin



class Especies(models.Model):
    descricao = models.CharField(verbose_name='Descrição', max_length=255)


    class Meta:
        verbose_name='Espécie'
        verbose_name_plural= 'Espécies'

    def __str__(self):
        return self.descricao



class Arvores(models.Model):
    especies = models.ForeignKey(Especies, on_delete=models.CASCADE)
    descricao = models.CharField(verbose_name='Descrição', max_length=255)
    idade = models.PositiveSmallIntegerField()


    class Meta:
        verbose_name='Árvore'
        verbose_name_plural= 'Árvores'

    def __str__(self):
        return self.descricao



class GrupoArvores(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=255)
    descricao = models.CharField(verbose_name='Descrição', max_length=255)
    arvores = models.ManyToManyField(Arvores)


    class Meta:
            verbose_name='Grupo de Árvores'
            verbose_name_plural= 'Grupo de Árvores'

    def __str__(self):
        return self.nome + ' - ' + self.descricao



class Colheita(models.Model):
    informacoes = models.CharField(verbose_name='Informações', max_length=255)
    data_colheita = models.DateField(auto_now=False, verbose_name='Data da Colheita')
    peso_bruto = models.DecimalField(decimal_places=3, max_digits=10)
    arvore = models.ForeignKey(Arvores, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Árvores')
    grupo_arvores = models.ForeignKey(GrupoArvores, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Grupo de Árvores')
    especies = models.ForeignKey(Especies, editable=False, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if not self.arvore and not self.grupo_arvores:
            raise Exception('Você não pode deixar os 2 campos vazios')
        self.especies = self.arvore.especies
        super().save(*args, **kwargs)

    def __str__(self):
        return self.informacoes

