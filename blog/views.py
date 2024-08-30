from rest_framework import generics
from rest_framework import status
from rest_framework import response
from .serializer import BlogSerializer
from .models import blog


class BlogViewApi(generics.ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        blogs = blog.objects.all()
        return blogs
