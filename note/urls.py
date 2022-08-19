from django.urls import path
from note import views

urlpatterns = [
    path('', views.noteListView, name='home'),
    path('note-add', views.NoteAddView.as_view(), name='note-add'),
    
]