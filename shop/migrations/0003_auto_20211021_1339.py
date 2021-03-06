# Generated by Django 3.2.7 on 2021-10-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210918_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='genus',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Основное фото цветка'),
        ),
        migrations.AlterField(
            model_name='item',
            name='availability',
            field=models.CharField(choices=[('AV', 'доступно'), ('EN', 'закончились'), ('RE', 'на размножении')], default='AV', max_length=2, verbose_name='Доступность'),
        ),
    ]
