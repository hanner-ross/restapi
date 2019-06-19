from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from usuarios import views

urlpatterns = [
    path('usuarios/$', views.UsuariosList.as_view()),
    path('usuarios/(?P<pk>[0-9]+)/$', views.UsuariosDetail.as_view()),
    path('tableros/$', views.TablerosList.as_view()),
    path('tableros/(?P<pk>[0-9]+)/$', views.TablerosDetail.as_view()),
    path('ideas/$', views.IdeasList.as_view()),
    path('ideas/(?P<pk>[0-9]+)/$', views.IdeasDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
