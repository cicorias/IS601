# Generated by Django 3.0.6 on 2020-06-09 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_auto_20200603_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='bakedgood',
            name='good_type',
            field=models.CharField(choices=[('BA', 'Bagel'), ('BR', 'Bread'), ('CO', 'Cookie'), ('CA', 'Cake'), ('PR', 'Pretzel')], default='CO', max_length=2),
            preserve_default=False,
        ),
    ]