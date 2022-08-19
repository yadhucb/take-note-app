from django.urls import path
from note import views

urlpatterns = [
    path('note-add', views.NoteAddView.as_view(), name='note-add'),
    
]