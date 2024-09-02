from rest_framework import serializers
from .models import blog, category_list


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category_list
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(many=True)
    username = serializers.CharField(source="user.username", read_only=True)
    image = serializers.SerializerMethodField("get_image_url")

    class Meta:
        model = blog
        fields = ["id", "username", "title", "description",
                  "image", "author", "created_at", "category"]

    def get_image_url(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url
        return request.build_absolute_uri(image_url)
