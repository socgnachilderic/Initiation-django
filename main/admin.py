from django.contrib import admin
from .models import Tutoriel

# Register your models here.

class TutorielAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Titre/Date', {'fields': ['tutoriel_titre', 'tutoriel_publier']}),
        ('Contenu', {'fields': ['tutoriel_contenu']})
    ]

admin.site.register(Tutoriel, TutorielAdmin)