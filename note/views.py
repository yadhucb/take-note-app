from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from note.models import Note
from note.forms import NoteForm

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
    notes = Note.objects.all()
    context = {
        'notes' : notes
    }
    return render(request, 'home.html', context)
