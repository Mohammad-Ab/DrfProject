#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUser,IsAuthorOrReadOnly,IsStaffOrReadOnly,IsSuperUserOrStaffReadOnly
from blog.models import Article
from .serializers import ArticleSerializer,UserSerializer
from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet

# Create your views here.
# class ArticleList(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
# class ArticleDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permissions_classes = (IsStaffOrReadOnly,IsAuthorOrReadOnly)

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #for permissions is diffrente

class UserList(ListCreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permissions_classes = (IsSuperUserOrStaffReadOnly,)



class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = (IsSuperUserOrStaffReadOnly,)

