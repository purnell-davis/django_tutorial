from django.db import models
from django.utils import timezone

class Post(models.Model):
    # ForeignKey - link to another model
    author = models.ForeignKey('auth.User')
    # CharField - Finite string space
    title = models.CharField(max_length=200)
    # TextField - More string space
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
