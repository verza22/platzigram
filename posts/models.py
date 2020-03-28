# Django
from django.db import models
from django.contrib.auth.models import User

# Models
from users.models import Profile

class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)