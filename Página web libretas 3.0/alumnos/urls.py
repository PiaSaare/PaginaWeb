#from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    path('index', views.index, name='index'),
    path('libretas',views.libretas, name='libretas'),
    path('about', views.about, name='about'),
    path('agendas', views.agendas, name='agendas'),
    path('carrito', views.carrito, name='carrito'),
    path('cuadernos', views.cuadernos, name='cuadernos'),
    path('libretasPerso', views.libretasPerso, name='libretasPerso'),
    path('registro', views.registro, name='registro'),
    path('crud', views.crud, name='crud'),
    path('alumnosAdd', views.alumnosAdd, name='alumnosAdd'),
]

