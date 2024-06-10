from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    topic = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, blank=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    abstract = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} on {self.post.title}"
    
