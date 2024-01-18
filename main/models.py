from django.db import models

# Create your models here.


class PortfolioModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    desc = models.TextField()
    