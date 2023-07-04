from rest_framework import serializers
from blog.models import Article
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        #exclude=['users']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = "__all__"
