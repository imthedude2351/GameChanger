# Generated by Django 3.2 on 2021-04-13 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_rating_game_rated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500)),
                ('rating', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.game')),
            ],
        ),
    ]