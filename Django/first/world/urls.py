from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('much', views.much, name='much'),
    path('see', views.see, name='see'),
    path('<str:name>', views.all, name='all')
]