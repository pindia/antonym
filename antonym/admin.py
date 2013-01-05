from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from antonym.models import Word, WordResponse

def make_active(modeladmin, request, queryset):
    queryset.update(status=Word.STATUS_ACTIVE)
make_active.short_description = 'Set selected words to active'

def make_inactive(modeladmin, request, queryset):
    queryset.update(status=Word.STATUS_INACTIVE)
make_inactive.short_description = 'Set selected words to inactive'

def make_rejected(modeladmin, request, queryset):
    queryset.update(status=Word.STATUS_REJECTED)
make_rejected.short_description = 'Reject selected words'

def view_responses(modeladmin, request, queryset):
    return HttpResponseRedirect(reverse('admin:antonym_wordresponse_changelist')+'?word__exact=%s' % queryset[0].id)

class WordAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ['status']
    actions = [make_active, make_inactive, make_rejected, view_responses]

class WordResponseAdmin(admin.ModelAdmin):
    list_display = ['word', 'response', 'date', 'ip']

admin.site.register(Word, WordAdmin)
admin.site.register(WordResponse, WordResponseAdmin)