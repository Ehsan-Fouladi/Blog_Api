from rest_framework import serializers
from .models import blog, Categories


class BlogCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
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
        if image_url:
            return request.build_absolute_uri(image_url)


class CategorySerializer(serializers.ModelSerializer):
    post = serializers.SerializerMethodField()

    class Meta:
        model = Categories
        fields = ["id", 'title', 'post']

    def get_post(self, obj):
        serializer = BlogSerializer(
            obj.category, context=self.context, many=True)
        return serializer.data
