from django.db import models
from django.forms import ModelForm


class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class BakedGood(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    type_choices = [
        ('BA', 'Bagel'),
        ('BR', 'Bread'),
        ('CO', 'Cookie'),
        ('CA', 'Cake'),
        ('PR', 'Pretzel'),
        ('OT', 'Other'),
    ]
    good_type = models.CharField(max_length=2, choices=type_choices, default='OT')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    recipe = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self) -> str:
        return self.name + ' fff'

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'desc': self.desc,
            'type': self.good_type,
            'price': self.price,
            'recipe': self.recipe,
            #  'ingredients': self.ingredients,
        }


class BakedGoodForm(ModelForm):
    class Meta:
        model = BakedGood
        fields = ['name', 'desc', 'good_type', 'price', 'recipe', 'ingredients']


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'desc']

