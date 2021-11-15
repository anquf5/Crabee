from django.contrib.auth.models import User
from django.db import models

# Create your models here.
TITLE_MAX_LENGTH = 128
CONTENT_MAX_LENGTH = 1000

class Topic(models.Model):
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    pub_time = models.DateTimeField(auto_now=True)
    topic_cont = models.CharField(max_length=CONTENT_MAX_LENGTH) # topic content
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pub_time',)

    def __str__(self):
        return self.title

class TopicReply(models.Model):
    pub_time = models.DateTimeField(auto_now=True)
    replier = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_cont = models.CharField(max_length=CONTENT_MAX_LENGTH) # reply content
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pub_time',)

    def __str__(self):
        return self.reply_cont