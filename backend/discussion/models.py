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

    def get_creator(self):
        un = User.objects.get(pk=self.creator_id).username
        return un

    def get_reply_num(self):
        num = TopicReply.objects.filter(topic=self).count()
        return num

    def get_last_replier(self):
        if TopicReply.objects.filter(topic_id=self.id):
            rid = TopicReply.objects.filter(topic_id=self.id).last().id
            return User.objects.get(pk=rid).username
        else:
            return ''

    def get_update_time(self):
        if TopicReply.objects.filter(topic_id=self.id):
            return TopicReply.objects.filter(topic_id=self).last().pub_time
        else:
            return self.pub_time


    def __str__(self):
        return self.title

class TopicReply(models.Model):
    pub_time = models.DateTimeField(auto_now=True)
    replier = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_cont = models.CharField(max_length=CONTENT_MAX_LENGTH) # reply content
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="reply")

    class Meta:
        ordering = ('pub_time',)

    def get_replier(self):
        un = User.objects.get(pk=self.replier_id).username
        return un

    def __str__(self):
        return self.reply_cont