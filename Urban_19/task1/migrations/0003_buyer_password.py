# Generated by Django 5.1.3 on 2024-11-19 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_alter_buyer_balance_alter_game_cost_alter_game_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='password',
            field=models.CharField(default=11111111, max_length=32),
        ),
    ]
