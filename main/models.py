from django.db import models

# Create your models here.


class PortfolioModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    desc = models.TextField()
    url = models.URLField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
    