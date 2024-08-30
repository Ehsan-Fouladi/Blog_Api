from rest_framework import serializers
from .models import blog, category_list


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category_list
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(many=True)

    class Meta:
        model = blog
        fields = ["user", "title", "description", "image", "author", "created_at", "category"]
