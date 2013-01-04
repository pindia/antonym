from django.contrib import admin
from antonym.models import Word, WordResponse

class WordAdmin(admin.ModelAdmin):
    list_display = ['name']

class WordResponseAdmin(admin.ModelAdmin):
    list_display = ['word', 'response', 'date', 'ip']

admin.site.register(Word, WordAdmin)
admin.site.register(WordResponse, WordResponseAdmin)