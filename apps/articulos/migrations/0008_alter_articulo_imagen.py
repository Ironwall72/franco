# Generated by Django 4.2.3 on 2023-07-22 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0007_alter_articulo_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, default='static/post_default.png', null=True, upload_to='media'),
        ),
    ]