from django.db import models

# Create your models here.
class source(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
