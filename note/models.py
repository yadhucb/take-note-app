from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to = 'note_images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:10]

