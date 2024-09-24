from django.urls import path
from . import views


urlpatterns = [
    path("blog/", views.ArticlesListApiView.as_view()),
    path("all/", views.AllArticlesApiView.as_view()),
    path("detail/<slug:slug>/", views.ArticlesDetailApiView.as_view()),
    path("category/<int:id>/", views.CategoryApiView.as_view()),
    path("search/", views.ArticlesSearchApiView.as_view())
]
