#from django.shortcuts import render
from rest_framework.generics import ListAPIView
from blog.models import Article
from .Serializers import ArticleSerializer

# Create your views here.
class ArticleList(ListAPIView):
    queryset = Article.objects.all()
    Serializer_class = ArticleSerializer
