# Generated by Django 4.2.2 on 2023-07-11 21:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('activo', models.BooleanField(default=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('actualizacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-nombre',),
            },
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('activo', models.BooleanField(default=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('actualizacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-nombre',),
            },
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('bajada', models.CharField(blank=True, max_length=600, null=True)),
                ('fecha_actualiz', models.DateTimeField(auto_now_add=True)),
                ('publicado', models.BooleanField(default=False)),
                ('contenido', models.TextField()),
                ('activo', models.BooleanField(default=True)),
                ('imagen', models.ImageField(blank=True, default='static/post_default.png', null=True, upload_to='media')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('categoria', models.ForeignKey(default='Sin categoría', null=True, on_delete=django.db.models.deletion.SET_NULL, to='articulos.categoria')),
                ('etiqueta', models.ForeignKey(default='Sin etiqueta', null=True, on_delete=django.db.models.deletion.SET_NULL, to='articulos.etiqueta')),
            ],
            options={
                'ordering': ('-fecha_creacion',),
            },
        ),
    ]
