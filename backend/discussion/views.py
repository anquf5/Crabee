from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
# Create your views here.
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Topic, TopicReply
from .serializers import TopicSerializer, TopicDetailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class TopicList(APIView):
    def get(self, request, format=None):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

class TopicDetail(APIView):
    def get(self, request, pk, format=None):
        topic = self.get_object(pk)
        serializer = TopicDetailSerializer(topic)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Topic.objects.get(pk=pk)
        except Topic.DoesNotExist:
            raise Http404

# Post topic
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
def add_topic(request):
    if request.user.id == None:
        request.user = User.objects.get(username="admin")

    topic_obj = Topic.objects.create(creator=request.user)
    topic_obj.title = request.data.get('title')
    topic_obj.topic_cont = request.data.get('content')
    topic_obj.save()
    return JsonResponse({'msg': 'OK'})

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
def add_reply(request):
    if request.user.id == None:
        request.user = User.objects.get(username="admin")

    topic = Topic.objects.get(pk=request.data.get('tid'))
    reply_obj = TopicReply.objects.create(topic=topic, replier=request.user)
    reply_obj.reply_cont = request.data.get('content')
    reply_obj.save()
    return JsonResponse({'msg': 'OK'})
