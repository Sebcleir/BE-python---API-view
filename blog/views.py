from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from wired.permissions import CustomPermission
from blog.models import Post
from blog.serializers import PostSerializer


def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})


@api_view(["GET", "POST", "PUT", "DELETE"])
@parser_classes([MultiPartParser])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, CustomPermission])
def post(request, pk=None):
    if request.method == "GET":
        if pk:
            post = Post.objects.get(id=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=200)
        else:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data, status=200)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Post created", status=201)
        else:
            return Response(serializer.errors, status=400)
    elif request.method == "PUT":
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Post updated", status=200)
        else:
            return Response(serializer.errors, status=400)
    elif request.method == "DELETE":
        # post = Post.objects.get(id=pk)
        # post.delete()
        if Post.objects.filter(id=pk).exists():
            Post.objects.filter(id=pk).delete()
            return Response("Post deleted", status=200)
        else:
            return Response("Post not found", status=404)
