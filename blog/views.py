from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import BlogSerializer, CategorySerializer
from .models import blog, Categories


class PostListApiView(generics.ListAPIView):
    """
    Post List View
    """
    serializer_class = BlogSerializer

    def get_queryset(self):
        blogs = blog.objects.all().order_by("-created_at")
        return blogs


class PostDetailApiView(APIView):
    """
    Post Detail View
    """

    def get(self, request, slug):
        post = get_object_or_404(blog, title=slug)
        serializer = BlogSerializer(post, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryApiView(APIView):
    """
    Category List View
    """

    def get(self, request, id):
        category = get_object_or_404(Categories, id=id)
        serializer = CategorySerializer(category, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
