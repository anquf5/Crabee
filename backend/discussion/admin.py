from django.contrib import admin
from .models import Topic, TopicReply
# Register your models here.

class repliesInline(admin.TabularInline):
    model = TopicReply
    fk_name = "topic"

class topic(admin.ModelAdmin):
    list_display = ['title','creator','pub_time']
    inlines = [repliesInline]

admin.site.register(Topic, topic)
admin.site.register(TopicReply)