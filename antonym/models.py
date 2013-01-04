from django.db import models

class Word(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)

    def __unicode__(self):
        return self.name

class WordResponse(models.Model):
    word = models.ForeignKey(Word)
    response = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    ip = models.IPAddressField()
    session = models.IntegerField()
    visible = models.BooleanField(default=True)