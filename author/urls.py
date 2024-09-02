from django.urls import path

from . import views
app_name = 'author'

urlpatterns = [
    path('',views.index, name='index'),
    path('add/', views.add_author, name='add'),
    path('<int:pk>/',views.detail, name="author")
]
