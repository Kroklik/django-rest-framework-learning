"""
URL configuration for drf_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from actors.views import ActorApiList, ActorApiUpdate, ActorApiDestroy
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'actors', ActorViewSet, basename='actors')
# print(router.urls)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/actors/', ActorApiList.as_view()),
    path('api/v1/actors/<int:pk>/', ActorApiUpdate.as_view()),
    path('api/v1/actordelete/<int:pk>/', ActorApiDestroy.as_view()),
    # path('api/v1/', include(router.urls)),
    # path('api/v1/actorslist', ActorViewSet.as_view({'get': 'list'}), name='actor_api'),
    # Вместо этого мы используем routers
    # path('api/v1/actorslist/<int:pk>/', ActorViewSet.as_view({'put': 'update'}), name=''),

]

# http://127.0.0.1:8000/api/v1/actors/
