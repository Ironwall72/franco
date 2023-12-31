from django.urls import path
from .views import PostListView, PostDetailView, DeletePostView, crearArticulo


app_name = 'apps.posts'

urlpatterns = [
    path('articulos/', PostListView.as_view(), name='articulos'),
    path('articulos/<int:id>/', PostDetailView.as_view(), name='articulo_ind'),
    path('crearArticulo/', crearArticulo),
    path('articulos/<int:id>/delete', DeletePostView.as_view(), name='delete_post'),
]
