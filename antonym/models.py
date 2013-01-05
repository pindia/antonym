from django.db import models

class Word(models.Model):
    STATUS_ACTIVE = 0
    STATUS_INACTIVE = 1
    STATUS_NEW = 2
    STATUS_REJECTED = 3
    name = models.CharField(max_length=50, db_index=True, unique=True)
    status = models.IntegerField(db_index=True, choices=((STATUS_ACTIVE, 'active'), (STATUS_INACTIVE, 'inactive'), (STATUS_NEW, 'new'), (STATUS_REJECTED, 'rejected')))
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class WordResponse(models.Model):
    word = models.ForeignKey(Word)
    response = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    ip = models.IPAddressField()
    session = models.IntegerField()
    visible = models.BooleanField(default=True)