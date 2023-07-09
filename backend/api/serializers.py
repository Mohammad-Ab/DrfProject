from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model
from drf_dynamic_fields import DynamicFieldsMixin


class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    def get_author(self,obj):
        return obj.author.username
    author = serializers.SerializerMethodField("get_author")
#     author=serializers.CharField(source="author.username") 

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
