from django.shortcuts import render, redirect
from .models import Articulo
from .forms import ArticuloForms
from django.contrib import messages
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
    model = Articulo
    template_name = 'articulos/articulos.html'
    context_object_name = 'articulos'

class PostDetailView(DetailView):
    model = Articulo
    template_name = 'articulos/articulo_ind.html'
    context_object_name = 'articulos'
    pk_url_kwarg = 'id'
    queryset = Articulo.objects.all()

def crearArticulo(request):
    data = {'form': ArticuloForms()}
    if request.method == 'POST':
        formulario = ArticuloForms( data = request.POST )
        if formulario.is_valid():
            formulario.save()
            
            # data['mensaje'] = 'Articulo guardado.'
            # messages.success(request, 'Los datos se han guardado correctamente.')
            return redirect('apps.posts:articulos')
        else:
            data['form'] = formulario
    return render(request, 'articulos/crearArticulo.html', data)

class DeletePostView(DeleteView):
    model = Articulo
    context_object_name = 'articulos'
    template_name = 'post/delete_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('apps.posts:articulos')

