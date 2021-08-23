from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="list"),
    path('update_todo/<str:pk>/', views.updateTodo, name="update_todo"),
    path('delete/<str:pk>/', views.deleteTodo, name="delete"),
]