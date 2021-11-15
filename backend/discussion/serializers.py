from .models import Topic, TopicReply
from rest_framework import serializers

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id',
                  'title',
                  'pub_time'
                  'creator',
                  'topic_cont'
                  )

class TopicReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicReply
        fields = ('pub_time',
                  'replier',
                  'reply_cont',
                  )