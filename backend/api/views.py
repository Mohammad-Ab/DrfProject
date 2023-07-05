#from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from .permissions import IsSuperUser,IsAuthorOrReadOnly,IsStaffOrReadOnly,IsSuperUserOrStaffReadOnly
from blog.models import Article
from .serializers import ArticleSerializer,UserSerializer
from django.contrib.auth.models import User

# Create your views here.
class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permissions_classes = (IsStaffOrReadOnly,IsAuthorOrReadOnly)

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = (IsSuperUserOrStaffReadOnly,)

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = (IsSuperUserOrStaffReadOnly,)
