from django.urls import path
from blog.views import home, post

urlpatterns = [
    path("", home),
    path("post/<int:pk>", post),
    path("post", post)
]
