from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.species})"

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to='post_pics/')
    created_at = models.DateTimeField(auto_now_add=True)
    # This is the modern way to handle likes:
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return f"Post by {self.author.username} at {self.created_at}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post}"