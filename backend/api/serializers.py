from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        #exclude=['users']
    def validate_title(self,value):
        filter_list=['java','php']
        for i in filter_list:
            if i in value:
                raise serializers.ValidationError("it's not real word!")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
