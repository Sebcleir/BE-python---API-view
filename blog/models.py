from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="media/blog/images", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


class File(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to="blog/files", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
