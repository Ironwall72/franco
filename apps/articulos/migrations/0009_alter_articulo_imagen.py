# Generated by Django 4.2.3 on 2023-07-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0008_alter_articulo_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, default='img/post_default.jpeg', null=True, upload_to='img/'),
        ),
    ]