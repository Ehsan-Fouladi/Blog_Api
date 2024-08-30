from django.db import models
from account.models import User


class category_list(models.Model):
    title = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.title


class blog(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_user")
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="blogs/images")
    author = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(category_list, related_name="category")


    def __str__(self) -> str:
        return f"username: {self.user.username}, Title: {self.title}"