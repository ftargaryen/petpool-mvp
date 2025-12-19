from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50) # e.g., Dog, Cat
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.species})"

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True) # Bonus feature
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.author.username} at {self.created_at}"