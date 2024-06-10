from django.urls import path
from .views import PostList, PostDetail, filter_by_topic, submit_comment, create_post, delete_comment, create_author

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/details/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('posts/topic/<str:topic>/', filter_by_topic, name='filter-by-topic'),
    path('comments/submit/', submit_comment, name='submit-comment'),
    path('posts/create/', create_post, name='create-post'),
    path('comments/delete/<int:comment_id>/', delete_comment, name='delete-comment'),
    path('authors/create/', create_author, name='create_author'),
]
