from django import forms
from note.models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'body',
            'image'
        ]
    # ===== widgets for styling form by using bootstrap class =========
        widgets = {
                'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' :'Title'}),
                'body' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' :'Take a Note'}),
                'image' : forms.FileInput(attrs={'class' : 'form-control d-none'}),
                
            }
