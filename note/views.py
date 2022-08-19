from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.db.models import Q
from note.models import Note
from note.forms import NoteForm
import os

# ===== adding new note by using model form ===========
class NoteAddView(View):

    def get(self, request):
        form = NoteForm
        context = {
            'form' : form
        }
        return render(request, 'note-add.html', context)

    def post(self, request):
        form = NoteForm(request.POST, request.FILES)
        context = {
            'form' : form
        }
        if form.is_valid():
            form.save()
            return redirect('home')
        messages.error(request, 'Form is not valid!')
        return render(request, 'note-add.html', context)

# ====== listing all available notes ========
def noteListView(request):
    notes = Note.objects.all().order_by('-updated_at')
    context = {
        'notes' : notes
    }
    return render(request, 'home.html', context)

# ====== take details of specific note =======
def noteDetailsView(request, *args, **kwargs):
    id = kwargs.get('pk')
    try:
        note = Note.objects.get(id = id)
        context = {
        'note' : note
        }
        return render(request, 'note-details.html', context)
    except:
        return redirect('home')

# ======== note search by title and body ===========
def noteSearchView(request):
    search_input = request.GET.get('search-input')
    notes = Note.objects.filter(
        Q(title__icontains = search_input) | 
        Q(body__icontains = search_input)).order_by('-updated_at')
    context = {
        'notes' : notes
    }
    return render(request, 'home.html', context)

# ====== edit a perticular note instance =======
class NoteEditView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        try:
            note_instance = Note.objects.get(id = id)
            form = NoteForm(instance=note_instance)
            context = {
                'form' : form,
                'image' : note_instance.image,
                'note' : note_instance
            }
            return render(request, 'note-edit.html', context)
        except:
            return redirect('home')

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        try:
            note_instance = Note.objects.get(id = id)
            form = NoteForm(request.POST, request.FILES, instance=note_instance)
            if form.is_valid():
                form.save()
                return redirect('home')
            context = {
                'form' : form
            }
            messages.error(request, 'Form is not valid!')
            return render(request, 'note-edit.html', context)
        except:
            return redirect('home')

# ====== delete a perticular note =======
def noteDeleteView(request, *args, **kwargs):
    id = kwargs.get('pk')
    try:
        note = Note.objects.get(id = id)
        note.delete()
        messages.info(request, 'Note deleted!')
        return redirect('home')
    except:
        return redirect('home')