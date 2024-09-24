from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import BlogSerializer, CategorySerializer
from .models import blog, Categories
from .pagination import StandardResultSetPagination, PostResultSetPagination, SearchResultSetPagination


class ArticlesListApiView(generics.ListAPIView):
    """
    Articles List View
    """
    serializer_class = BlogSerializer
    pagination_class = PostResultSetPagination

    def get_queryset(self):
        blogs = blog.objects.all().order_by("-created_at")
        return blogs


class AllArticlesApiView(generics.ListAPIView):
    """
    All Articles Pagination
    """
    serializer_class = BlogSerializer
    pagination_class = StandardResultSetPagination

    def get_queryset(self):
        blogs = blog.objects.all().order_by("-created_at")
        return blogs


class ArticlesDetailApiView(APIView):
    """
    Articles Detail View
    """
    serializer_class = BlogSerializer

    def get(self, request, slug):
        post = get_object_or_404(blog, title=slug)
        serializer = BlogSerializer(post, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryApiView(APIView):
    """
    Category List View
    """
    serializer_class = CategorySerializer

    def get(self, request, id):
        category = get_object_or_404(Categories, id=id)
        serializer = CategorySerializer(category, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticlesSearchApiView(APIView, SearchResultSetPagination):
    """
    Search Article with method q Example:/blog/search/?q=javascript
    """
    serializer_class = BlogSerializer

    def get(self, request):
        q = request.GET.get('q')
        queryset = blog.objects.filter(Q(title=q) | Q(description=q))
        result = self.paginate_queryset(queryset, request)
        serializer = BlogSerializer(result, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
