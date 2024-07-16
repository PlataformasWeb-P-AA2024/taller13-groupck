from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_edificios, name='lista_edificios'),
    path('departamentos', views.lista_departamentos, name='lista_departamentos'),
    path('edificio/nuevo/', views.edificio_nuevo, name='edificio_nuevo'),
    path('edificio/<int:pk>/editar/', views.edificio_editar, name='edificio_editar'),
    path('edificio/<int:pk>/eliminar/', views.edificio_eliminar, name='edificio_eliminar'),
    path('departamento/nuevo/', views.departamento_nuevo, name='departamento_nuevo'),
    path('departamento/<int:pk>/editar/', views.departamento_editar, name='departamento_editar'),
    path('departamento/<int:pk>/eliminar/', views.departamento_eliminar, name='departamento_eliminar'),
]