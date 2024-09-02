from django.db import models
from account.models import User


class Categories(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class blog(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_user")
    title = models.SlugField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="blogs/images")
    author = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Categories, related_name="category")

    class Meta:
        ordering = ["-title"]

    def __str__(self) -> str:
        return f"username: {self.user.username}, Title: {self.title}"
