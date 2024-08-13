import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser

from .models import Actor
from rest_framework.renderers import JSONRenderer


class ActorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Actor
        fields = '__all__'

# class ActorModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# class ActorSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField(max_length=512)
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     category_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Actor.objects.create(
#             **validated_data)  # validated_data - словарь из всех проверенных данных которые пришли из post запроса
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.updated_at = validated_data.get("updated_at", instance.updated_at)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.category_id = validated_data.get("category_id", instance.category_id)
#         instance.save() # - сохранили нашего обновленного актера
#         return instance
#
#     def delete(self, instance):
#         instance.delete()
#         return instance



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
