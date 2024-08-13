from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .models import Actor, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import ActorSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class ActorApiList(generics.ListCreateAPIView):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ActorApiUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


class ActorApiDestroy(generics.RetrieveDestroyAPIView):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
# class ActorViewSet(viewsets.ModelViewSet):
#     serializer_class = ActorSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Actor.objects.all()[:3]
#         return Actor.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=True)
#     def categories(self, request, pk=None):
#         categories = Category.objects.get(id=pk)
#         return Response({'categories': categories.name})

# class ActorApiList(generics.ListCreateAPIView):
#     queryset = Actor.objects.all()
#     serializer_class = ActorSerializer
#
# class ActorApiUpdate(generics.UpdateAPIView):
#     queryset = Actor.objects.all()
#     serializer_class = ActorSerializer
#
#
# class ActorApiDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Actor.objects.all()
#     serializer_class = ActorSerializer

# class ActorApiView(APIView):
#     def get(self, request):
#         lst = Actor.objects.all()
#         return Response({'posts': ActorSerializer(lst, many=True).data})
#
#     def post(self, request):
#         serializer = ActorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()  # Говорим что хотим вызывать метод save, который мы создали в serializers.py в ActorSerializer
#         return Response({'post': serializer.data})  # - получаем пост который мы создали
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Put method не разрешен"})  # - если нету pk вызываем ошибку
#         try:
#             instance = Actor.objects.get(pk=pk)  # - Пробуем взять актера по pk
#         except Exception as e:
#             return Response({"error": "Объект не существует"})
#
#         serializer = ActorSerializer(data=request.data,
#                                      instance=instance)  # - Вызываем наш serializer и передаем туда data, instance. Serializer сам поймет что нужно использовать функцию put, так как мы дали аргументы data и insatance
#         serializer.is_valid(raise_exception=True)  # - Проверяем правильные ли данные
#         serializer.save()
#         return Response({"post": serializer.data})  # - Возвращаем наш обновленный пост
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Delete method не разрешен"})  # - если нету pk вызываем ошибку
#         try:
#             instance = Actor.objects.get(pk=pk)  # - Пробуем взять актера по pk
#         except Exception as e:
#             return Response({"error": "Объект не существует"})
#         serializer = ActorSerializer(instance=instance)  # Вызываем наш метод delete
#         serializer.delete(
#             instance=instance)  # удаляем наш объект из бд, instance - это объекто который мы получили по id из бд
#         return Response({"delete": f'Удален пользователь с pk - {pk}'})

# class ActorApiView(generics.ListAPIView):
#     queryset = Actor.objects.all()
#     serializer_class = ActorSerializer

# class ActorApiView(APIView):
#     def get(self, request):
#         lst = Actor.objects.all()
#         return Response({'posts': ActorSerializer(lst, many=True).data})
#
#     def post(self, request):
#         post_new = Actor.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#             category_id=request.data['category_id']
#         )
#         return Response({'new_post': ActorSerializer(post_new).data})
