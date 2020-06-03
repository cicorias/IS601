from django.db import models

class BakedGood(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    good_type = models.TextChoices('type', 'BAGEL BREAD COOKIE CAKE PRETZEL')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    recipe = models.TextField()
