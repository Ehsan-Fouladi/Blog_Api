from django.urls import path
from . import views


urlpatterns = [
    path("blog/", views.PostListApiView.as_view()),
    path("detail/<slug:slug>/", views.PostDetailApiView.as_view()),
    path("category/<int:id>/", views.CategoryApiView.as_view())
]
