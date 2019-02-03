from django.contrib import admin
from .models import Tutoriel
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class TutorielAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Titre/Date', {'fields': ['tutoriel_titre', 'tutoriel_publier']}),
        ('Contenu', {'fields': ['tutoriel_contenu']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Tutoriel, TutorielAdmin)