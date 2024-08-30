from django.urls import path
from . import views


urlpatterns = [
    path("blog/", views.BlogViewApi.as_view())
]
