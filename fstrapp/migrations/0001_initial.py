# Generated by Django 4.2.11 on 2024-04-07 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=4, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=10)),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(choices=[(' ', ' '), ('1A', '1A'), ('2A', '2A'), ('3A', '3A'), ('4A', '4A')], default=' ', max_length=2)),
                ('summer', models.CharField(choices=[(' ', ' '), ('1A', '1A'), ('2A', '2A'), ('3A', '3A'), ('4A', '4A')], default=' ', max_length=2)),
                ('autumn', models.CharField(choices=[(' ', ' '), ('1A', '1A'), ('2A', '2A'), ('3A', '3A'), ('4A', '4A')], default=' ', max_length=2)),
                ('spring', models.CharField(choices=[(' ', ' '), ('1A', '1A'), ('2A', '2A'), ('3A', '3A'), ('4A', '4A')], default=' ', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=128, unique=True)),
                ('phone', models.IntegerField()),
                ('fam', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('otc', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'новый объект'), ('pending', 'модерация работает'), ('accepted', 'модерация прошла успешно'), ('rejected', 'модерация прошла, информация не принята')], default='new', max_length=25)),
                ('beauty_title', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('other_titles', models.CharField(max_length=255)),
                ('connect', models.TextField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('coord_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fstrapp.coords')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fstrapp.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='fstrapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('data', models.ImageField(upload_to='media/')),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fstrapp.pereval')),
            ],
        ),
    ]
