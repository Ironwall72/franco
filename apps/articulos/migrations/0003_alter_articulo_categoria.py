# Generated by Django 4.2.3 on 2023-07-21 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0002_rename_bajada_articulo_subtitulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='articulos.categoria'),
        ),
    ]
