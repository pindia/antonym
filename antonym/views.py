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
    words = Word.objects.all()
    return render_template('index.html', request, words=words)

@csrf_exempt
def respond(request, word, response):
    word = Word.objects.get(name=word)
    try:
        session = int(request.GET.get('session', 0))
    except ValueError:
        session = 0
    ip = request.META['REMOTE_ADDR']
    #if WordResponse.objects.filter(word=word, ip=ip).count() <= 5: # protect vs the most mindless spam
    WordResponse.objects.create(word=word, ip=ip, session=session, response=response, visible=response not in settings.PROFANITIES_LIST)
    data = WordResponse.objects.filter(word=word, visible=True).values('response').annotate(count=Count('response')).order_by('-count')[:5]
    return HttpResponse(json.dumps(list(data)))
