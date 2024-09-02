from rest_framework import serializers
from .models import blog, category_list
from account.models import User

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category_list
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(many=True)
    username = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = blog
        fields = ["id", "username", "title", "description", "image", "author", "created_at", "category"]
