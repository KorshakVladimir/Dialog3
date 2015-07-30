from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=150,verbose_name=u'Имя')
    location  = models.ImageField(blank=True, null=True,verbose_name=u'Фон')
    person  = models.ImageField(blank=True, null=True,verbose_name=u'персонаж')
    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

    def __str__(self):
        return self.name