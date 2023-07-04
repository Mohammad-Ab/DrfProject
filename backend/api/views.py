#from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from blog.models import Article
from .serializers import ArticleSerializer,UserSerializer
from django.contrib.auth.models import User

# Create your views here.
class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
class ArticleDetail(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
