from django.db import models


class BakedGood(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    good_type = models.TextChoices('type', 'BAGEL BREAD COOKIE CAKE PRETZEL')
    sTypes = models.CharField(
        blank=True, choices=good_type.choices, max_length=20)   
    price = models.DecimalField(max_digits=6, decimal_places=2)
    recipe = models.TextField()

    def __str__(self):
        return 'Name: ' + self.name


class OtherBakedGood(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    goodType = models.TextChoices(
        'goodType', 'BAGEL BREAD COOKIE CAKE PRETZEL')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    recipe = models.TextField()
