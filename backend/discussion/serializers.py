from .models import Topic, TopicReply
from rest_framework import serializers

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id',
                  'title',
                  'get_username',
                  'get_reply_num',
                  'get_last_replier',
                  'get_update_time',
                  'get_absolute_url'
                  )

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicReply
        fields = ('id',
                  'get_pubtime',
                  'get_username',
                  'reply_cont',
                  'get_user_avatar',
                  )

class TopicDetailSerializer(serializers.ModelSerializer):
    reply = ReplySerializer(many=True)

    class Meta:
        model = Topic
        fields = ('title',
                  'get_pubtime',
                  'get_username',
                  'topic_cont',
                  'reply',
                  'get_user_avatar',
                  )