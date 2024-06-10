from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Author, Post, Comment
from .serializers import AuthorSerializer, PostSerializer, CommentSerializer

# Using ListAPIView for listing posts
class PostList(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-publish_time')
    serializer_class = PostSerializer

# Using RetrieveAPIView for getting details of a post
class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
# This function is used to filter posts by topic
@api_view(['GET'])
def filter_by_topic(request, topic):
    posts = Post.objects.filter(topic=topic)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

# This function is used to to submit a comment
@api_view(['POST'])
def submit_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# This function is used to to creat a post
@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# This function is used to to delete a commengt
@api_view(['DELETE'])
def delete_comment(request, comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()
        return Response({'message': 'Comment deleted successfully'}, status=204)
    except Comment.DoesNotExist:
        return Response({'message': 'Comment not found'}, status=404)

# This function is used to to creat an author
@api_view(['POST'])
def create_author(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
