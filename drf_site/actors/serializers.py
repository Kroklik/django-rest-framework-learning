import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser

from .models import Actor
from rest_framework.renderers import JSONRenderer


# class ActorModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class ActorSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=512)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()


# def encode():
#     model = ActorModel(title='Pipidastr', content='sigma')
#     model_sr = ActorSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title": "Terminator", "content": "Content: sigma"}')
#     data = JSONParser().parse(stream)
#     serializer = ActorSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
