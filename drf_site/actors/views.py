from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from .models import Actor
from .serializers import ActorSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

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

class ActorApiView(APIView):
    def get(self, request):
        lst = Actor.objects.all()
        return Response({'posts': ActorSerializer(lst, many=True).data})

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            post_new = Actor.objects.create(
                title=serializer.validated_data['title'],
                content=serializer.validated_data['content'],
                category_id=serializer.validated_data['category_id']
            )
            return Response({'new_post': ActorSerializer(post_new).data}, status=201)
        return Response(serializer.errors, status=400)