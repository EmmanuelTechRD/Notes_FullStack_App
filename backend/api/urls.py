from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NoteListCreateView.as_view(), name='list-create-note'),
    path('notes/delete/<int:pk>/', views.NoteDeleteView.as_view(), name='delete-note'),
]