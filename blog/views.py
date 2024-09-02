from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import BlogSerializer
from .models import blog


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
        return Response(serializer.data)
