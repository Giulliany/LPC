# Generated by Django 2.2.7 on 2019-11-07 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='seguidores',
            field=models.ManyToManyField(to='app_blog.Pessoa', verbose_name='Seguidores'),
        ),
    ]