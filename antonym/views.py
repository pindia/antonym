import json
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt

from antonym.models import Word, WordResponse

from django.conf import settings

def render_template(template, request, **kwds):
    return render_to_response(template, kwds, context_instance=RequestContext(request))

def index(request):
    words = Word.objects.filter(status=Word.STATUS_ACTIVE)
    return render_template('index.html', request, words=words)

def add(request):
    if request.method == 'POST':
        word = request.POST['word']
        status = Word.STATUS_REJECTED if any(p.match(word) for p in settings.PROFANITIES_LIST) else Word.STATUS_NEW
        Word.objects.get_or_create(name=word, defaults={'status': status})
        return render_template('add.html', request, submitted=True)
    return render_template('add.html', request)

def word_list(request):
    words = Word.objects.filter(status=Word.STATUS_ACTIVE).order_by('name')
    return render_template('list.html', request, words=words)

@csrf_exempt
def respond(request, word, response):
    word = Word.objects.get(name=word)
    try:
        session = int(request.REQUEST.get('session', 0))
    except ValueError:
        session = 0
    ip = request.META['REMOTE_ADDR']
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR'].split(',')[0].strip()
    response = response.strip()
    visible = not any(p.match(response) for p in settings.PROFANITIES_LIST)
    #if WordResponse.objects.filter(word=word, ip=ip).count() <= 5: # protect vs the most mindless spam
    WordResponse.objects.create(word=word, ip=ip, session=session, response=response, visible=visible)
    data = WordResponse.objects.filter(word=word, visible=True).values('response').annotate(count=Count('response')).order_by('-count')[:5]
    return HttpResponse(json.dumps(list(data)))
