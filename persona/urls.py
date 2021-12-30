from django.urls import path
from persona  import views
urlpatterns = [
    path('persona/', views.PersonaLista.as_view()),
    path('persona/<int:pk>', views.PersonaAPI.as_view()),
    path('pelicula/', views.peliculas_lista),
    path('pelicula/<int:pk>', views.peliculas_detalle)
]
