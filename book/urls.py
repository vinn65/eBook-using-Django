from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('add/',views.add,name="add"),
    path('',views.index,name="index"),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/edit/', views.edit, name="edit"),
    path('<int:pk>/delete', views.delete, name="delete"),
    
]
