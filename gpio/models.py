from django.db import models

from django.db import models

class Board(models.Model):
    numero = models.IntegerField(unique=True, null=False, default = 1, blank=False)
    nom = models.CharField(max_length=255,unique=True, null=True, blank=False)
    code = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return f'{self.nom}-{self.numero}'

class Pins(models.Model):
    nom = models.CharField(max_length=255, null=True, blank=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    gpio = models.IntegerField()
    state = models.IntegerField()

    class Meta:
        unique_together = ('board', 'gpio')

