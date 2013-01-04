from django.db import models

class Word(models.Model):
    name = models.CharField(max_length=50, db_index=True)

class WordResponse(models.Model):
    word = models.ForeignKey(Word)
    response = models.CharField(max_length=50)
    ip = models.IPAddressField()
    session = models.IntegerField()
    visible = models.BooleanField(default=True)