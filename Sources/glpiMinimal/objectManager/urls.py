from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('list/', views.object_list, name = "object_list"),
    path('add/', views.add_object, name = "add_object")
]
