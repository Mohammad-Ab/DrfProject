#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUser,IsAuthorOrReadOnly,IsStaffOrReadOnly,IsSuperUserOrStaffReadOnly
from blog.models import Article
from .serializers import ArticleSerializer,UserSerializer
from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet

# Create your views here.

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #for permissions is diffrente
    def get_permission(self):
        if self.action in ['list','create']:
            permissions_classes = [IsStaffOrReadOnly]
        else:
            permissions_classes = [IsStaffOrReadOnly,IsAuthorOrReadOnly]
        return [permission() for permission in permissions_classes]

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [IsSuperUserOrStaffReadOnly]

